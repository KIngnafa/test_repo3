#!/usr/bin/python


#imported modules
import os
import shutil
import sys
import time


#function declaration
def database_backup():
   timestring=time.localtime()
   TS=time.strftime("%d%m%Y%H%M%S",timestring)
   print(TS)
   backup_base="/backup/AWSSEP23/APEXDB"
   runner="YINKAR"
   backup_dir=os.path.join(backup_base,runner)

   try:
		#creating par file and writing into it 
      file=open("/home/oracle/scripts/practicedir_ynr_sep23/export_stack_temp_%s.par"%(TS),"w+")
      file.write("userid='/ as sysdba'\nschemas=stack_temp\ndumpfile=stack_temp_%s.dmp\nlogfile=stack_temp_%s.log\ndirectory=DATA_PUMP_DIR"%(TS,TS))
      file.close()

      file_read=open("/home/oracle/scripts/practicedir_ynr_sep23/export_stack_temp_%s.par"%(TS),"r+")
      file_content=file_read.read()

      print(file_content)
      file_read.close()
      file_name="export_stack_temp_%s.par"%(TS)
      file_path=os.path.join(os.getcwd(),"%s"%(file_name))

		#creating .sh file
      export=open("/home/oracle/scripts/practicedir_ynr_sep23/export.sh","w+")
      export.write(". /home/oracle/scripts/oracle_env_APEXDB.sh\nexpdp parfile=export_stack_temp_%s.par"%(TS))
      export.close()
      export_content="/home/oracle/scripts/practicedir_ynr_sep23/export.sh"

      if os.path.isfile(file_path):
         print("Par file exists")
      backup_path=os.path.join(backup_dir,TS)
      print(backup_path)
      os.popen("mkdir -p %s"%(backup_path))
      os.popen("chmod 700 %s"%(export_content))
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


#variable declaration





#main body
if __name__=="__main__":
	
	

















