#!/usr/bin/python


#imported modules
import os
import shutil
import sys
import time
import subprocess
#function declaration
def database_backup(a,b,c,d,e):
	timestring=time.localtime()
	TS=time.strftime("%d%m%Y%H%M%S",timestring)
	print(TS)
	backup_base=e
	runner=b
	backup_dir=os.path.join(backup_base,runner)
	backup_path=os.path.join(backup_dir,TS)
	
	dbstatus_path="%sdblogin.sh"%(d)
		
	#process commands and variables
	ps_command="ps -ef | grep pmon | grep APEXDB"
	output=subprocess.getoutput(ps_command)
	
	#schema export variables
	export_dmp="%s_%s_%s.dmp"%(a,b,TS)
	export_log="%s_%s_%s.log"%(a,b,TS)
	exportlog_path=os.path.join(backup_base,export_log)
	
	tar_name="%s%s_%s_%s.tar"%(backup_base,a,b,TS)
	file_path="%sdb_status.log"%(d)

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
			print("par file creation unscuccessful")

		try:
			#getting absolute path ofr .par file
			par_path=os.path.join(os.getcwd(),"%s"%(par_name))			
	
			#creating .sh file to set environment variables and start db schema backup
			export=open("%sexport_%s.sh"%(d,TS),"w+")
			export.write(". /home/oracle/scripts/oracle_env_APEXDB.sh\nexpdp parfile=%sexport_%s_%s_%s.par"%(d,a,b,TS))
			
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
			#creating .sh file to tar export files
			tar=open("%star_export.sh"%(d),'w+')
			tar.write("cd %s\n"%(backup_base))
			tar.write("tar -cvf %s %s %s --remove-files"%(tar_name,export_dmp,export_log))
			tar.close()
			tar_path="%star_export.sh"%(d) 
			os.popen("chmod 700 %s"%(tar_path))
			subprocess.call(['sh',"%s"%(tar_path)])
		except:
			print("tarring of %s and %s unsuccessful!"%(export_dmp,export_log)) 	
				
	else:
		print("Database is not running")

def backup_f_d(a,b,c):
	timestring=time.localtime()
	TS=time.strftime("%d%m%Y%H%M%S",timestring)
	dest_dir="%s/%s/%s/"%(b,c,TS)
	dest_path=os.path.join(os.getcwd(),dest_dir)
	#creating directory path if it doesnt exist yet
	
	os.makedirs(dest_path, exist_ok=True)	
	if os.path.isdir(a):
		#priting to  stdout
		print("Copying source directory %s to %s"%(a,dest_path))
      #using shutil copytree to copy a directory and its contents to destination dir
		shutil.copytree(a,dest_path)
	
	elif os.path.isfile(a):
      #printing to stdout
		print("Copying source file %s to %s"%(a,dest_path))

      #using shutil copy function to copy src to dst
		shutil.copy(a,dest_path)

      #printing to stdout
		print("Copy complete!")




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















