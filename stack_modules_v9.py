#!/usr/bin/python


#imported modules
import os
import shutil
import sys
import time
import subprocess
import tarfile
import gzip
import tempfile

#variable declaration
timestring=time.localtime()
TS=time.strftime("%d%m%Y%H%M%S",timestring)

#function declaration
def database_backup(a,b,c,d,e,f):
	#variable declaration
	backup_base=e
	runner=b
	
	#absolute path .dblogin.sh
	dbstatus_path="%sdblogin.sh"%(d)
		
	
	#schema export variables
	export_dmp="%s_%s_%s.dmp"%(a,b,TS)
	export_log="%s_%s_%s.log"%(a,b,TS)
	exportdmp_path=os.path.join(backup_base,export_dmp)
	exportlog_path=os.path.join(backup_base,export_log)
	
	#absolute path for db_status.log file
	file_path="%sdb_status.log"%(d)

	try:
   	#process command and variable
		ps_command="ps -ef | grep pmon | grep %s"%(f)
		output=subprocess.getoutput(ps_command)
	except subprocess.CalleddProcessError as e:
		print("Error executing command: %s"%(e))
	
	#checking is the database process is running and started up
	if output:
		print("Database is running!")	
		os.popen(dbstatus_path)
		
		#opening db_status.log file in read mode
		with open(file_path,'r') as dblog:
			file_contents=dblog.read()
			
		#checking if "OPEN" string is present in the file contents
		if "OPEN" in file_contents:
			print("Database is Open!")
		else:
			print("Database is not Open!")

		try:
			#creating .par file 
			par=open("%sexport_%s_%s_%s.par"%(d,a,b,TS), "w+")
			par.write("userid='/ as sysdba'\n")
			par.write("schemas=%s\n"%(a))
			par.write("dumpfile=%s_%s_%s.dmp\n"%(a,b,TS))
			par.write("logfile=%s_%s_%s.log\n"%(a,b,TS))
			par.write("directory=%s"%(c))
			par.close()
			par_read=open("%sexport_%s_%s_%s.par"%(d,a,b,TS),"r+")
			par_content=par_read.read()
			print(par_content)
			par_read.close()
			par_name="export_%s_%s_%s.par"%(a,b,TS)
			print(par_name)
		except:
			print("par file creation unsuccessful")

		try:
			#getting absolute path of .par file
			par_path=os.path.join(os.getcwd(),"%s"%(par_name))			
	
			#creating .sh file to set environment variables and start db schema backup
			export=open("%sexport_%s.sh"%(d,TS),"w+")
			export.write(". /home/oracle/scripts/oracle_env_%s.sh\nexpdp parfile=%sexport_%s_%s_%s.par"%(f,d,a,b,TS))
			
			export.close()
			export_content="%sexport_%s.sh"%(d,TS)	
			os.popen("chmod 700 %s"%(export_content))
		except:
			print("%s file creation failed"%(export_content))

		try:
			#start DB schema backup using expdp command
			print("Starting Schema export for %s"%(a))
			subprocess.call(['sh',"%s"%(export_content)])		
		except:
				print("expdp backup failed")

		#opening log file in read mode
		with open(exportlog_path,'r') as exportlog:
			exportlog_contents=exportlog.read()
		
		#checking for "successfully completed" string in export_log
		if "successfully completed" in  exportlog_contents:
			print("expdp backup successful")
		else:
			print("expdp backup failed")	

		try:
			#calling G_zipp function to zip dumpfile	
			G_zipp(exportdmp_path)
		except:
			print("tarring of %s and %s unsuccessful!"%(export_dmp,export_log)) 	
				
	else:
		print("Database is not running")

def backup_f_d(a,b,c):
	dest_dir="%s/%s/%s/"%(b,c,TS)
	dest_path=os.path.join(os.getcwd(),dest_dir)
	#creating directory path if it doesnt exist yet

	#making destination path if it doesn't exist	
	os.makedirs(dest_path, exist_ok=True)	
	if os.path.isdir(a):
		try:
      	#priting to  stdout
			print("Copying source directory %s to %s"%(a,dest_path))
      	#using shutil copytree to copy a directory and its contents to destination dir
			shutil.copytree(a,dest_path)
		except:
			print("Copying of source directory %s to %s failed"%(a,dest_path))
	elif os.path.isfile(a):
		try:
      	#printing to stdout
			print("Copying source file %s to %s"%(a,dest_path))

      	#using shutil copy function to copy src to dst
			shutil.copy(a,dest_path)

      	#printing to stdout
			print("Copy complete!")
		except:
			print("Copying of source file %s to %s has failed")

def disk_utilization_check(a,b):
	#output of subprocess.getoutput is stored in disk_util variable and type casted to an Integer
	disk_util=int(subprocess.getoutput(("df -h|grep '%s'|awk '{print $4}'|sed 's/%%//g'"%(a))))
	try:
		if disk_util > b:
			print("disk utilization for %s is above %s!"%(a,b))
		else:
			print("disk utilization for %s is below %s!"%(a,b))
	except:
		print("Disk utililization check failed")

def G_zipp(a):
	file_name=os.path.basename(a)
	dir_name=os.path.dirname(a)
	try:
		#checking if the source is a file
		if os.path.isfile(a):
			tar_file="%s.tgz"%(a)
			with tarfile.open(tar_file,'w:gz') as tar:
				tar.add(a,arcname=os.path.basename(a))

			print("%s has been succcessfully Gzipped!"%(file_name))
		elif os.path.isdir(a):
			tar_dir="%s.tgz"%(a)
  			#creates and opens a tar archive with gzip compression in write mode
			with tarfile.open(tar_dir, "w:gz") as tar:
				tar.add(a,arcname=os.path.basename(a))

			print("%s has been successfully Gzipped!"%(file_name))
	except:
		print("%s has failed to Gzip"%(file_name))

def unzipp(a,b):
	try:
		#opens specified tar archive
		file=tarfile.open(a)
		print(file.getnames())

      #extracts the content of the tar archive to the destination path
		file.extractall(b)

      #close tar archive
		file.close()
		print("%a has successfully been unzipped!"%(a))
	except:
		print("%s has failed to unzip!"%(a))

#main body
if __name__=="__main__":
	
	if function == "database_backup":
		schema=sys.argv[2]
		runner=sys.argv[3]
		directory=sys.argv[4]
		par_dir=sys.argv[5]
		sourcedb_physical=sys.argv[6]

		#calling function with required arguements
		database_backup(schema,runner,directory,par_dir,sourcedb_physical)
	elif function == "file_directory_cp":
		src=sys.argv[2]
		dst=sys.argv[3]
	
		file_directory_cp(src,dst)















