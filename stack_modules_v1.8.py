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

  	try:
		#creating .par file
		par=open("%sexport_%s_%s_%s.par"%(d,a,b,TS),"w+")
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
		#getting absolute path ofr .par file
		par_path=os.path.join(os.getcwd(),"%s"%(par_name))
		
		#creating .sh file to set environment variables and start db schema backup
		export=open("%sexport.sh"%(d),"w+")
		export.write(". /home/oracle/scripts/oracle_env_APEXDB.sh\nexpdp parfile=%sexport_%s_%s_%s.par"%(d,a,b,TS))
		export.close()
		export_content="%s/export.sh"%(d)
	
		if os.path.isfile(par_path):
			print("Par file exists")
		backup_path=os.path.join(backup_dir,TS)
		print(backup_path)

		#creating dir if it doesnt exist
		os.popen("mkdir -p %s"%(backup_path))
		#making .sh file executable
		os.popen("chmod 700 %s"%(export_content))
		#running .sh file to start db schema backup
		os.popen("%s"%(export_content))
	except:   
		print("Export failed")


def file_directory_cp(a,b):
   if os.path.isdir(a):
      #priting to  stdout
      print("Copying source directory %s to %s"%(a,b))
      #using shutil copytree to copy a directory and its contents to destination dir
      shutil.copytree(a,b)
   else:
      #printing to stdout
      print("Copying source file %s to %s"%(a,b))

      #using shutil copy function to copy src to dst
      shutil.copy(a,b)

      #printing to stdout
      print("Copy complete!")

def disk_utilization_check(a,b):
	#output of subprocess.getoutput is stored in disk_util variable and type casted to an Integer
	disk_util=int(subprocess.getoutput(("df -h|grep '%s'|awk '{print $4}'|sed 's/%%//g'"%(a))))
	if disk_util > b:
		print("disk utilization for %s is above %s!"%(a,b))
	else:
		print("disk utilization for %s is below %s!"%(a,b))
			
		

#main body
if __name__=="__main__":
	#variable declaratio
	function=sys.argv[1]
		
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















