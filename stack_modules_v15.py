#!/usr/bin/python


#imported modules
import os
import shutil
import sys
import time
import subprocess
import tarfile
import gzip
import smtplib
import time
import datetime
import cx_Oracle

#variable declaration
timestring=time.localtime()
TS=time.strftime("%d%m%Y%H%M%S",timestring)


#function declaration
def STACK_EMAIL(**args):
	try:
		FROM='oracle@MKIT-DEV-OEM.localdomain'
     #variables
		TO_EMAIL=args["email_add"]
		SUBJECT="%s %s: %s"%(args["function"],TS,args["status"])
		
		if args["status"] == "success":
			BODY="%s for %s was a %s!"%(args["function"],args["runner"],args["status"])
		else:
			BODY="%s for %s was a %s!"%(args["function"],args["runner"],args["status"])
			
		MSG=("\n".join(("From: %s" %FROM, "To: %s" %TO_EMAIL, "Subject: %s:\n" %SUBJECT,"%s" %BODY)))

		with smtplib.SMTP('localhost') as my_server:
			my_server.sendmail(FROM,TO_EMAIL,MSG)
		print("Email sent successfully to %s" %TO_EMAIL)
	except:
		print("Email was not sent.")

def database_backup(**args):
	OP_ID=1
	OP_NAME="EXPORT"
	OP_TYPE="BACKUP"
	backup_base=args["sourcedb_physical"]
	runner=args["runner"]
	
	#absolute path .dblogin.sh
	dbstatus_path="%sdblogin.sh"%(args["par_dir"])
		
	#schema export variables
	export_dmp="%s_%s_%s.dmp"%(args["schema"],args["runner"],TS)
	export_log="%s_%s_%s.log"%(args["schema"],args["runner"],TS)
	exportdmp_path=os.path.join(backup_base,export_dmp)
	exportlog_path=os.path.join(backup_base,export_log)

	#path to db_status.log file	
	file_path="%sdb_status.log"%(args["par_dir"])
	
	STATUS="RUNNING"
	db_connection(schema_pass=args["schema_pass"],schema=args["schema"],OP_ID=OP_ID,OP_NAME=OP_NAME,OP_TYPE=OP_TYPE,RUNNER=args["runner"],STATUS=STATUS,dbname=args["dbname"])
	try:
		#process command and variable
		ps_command="ps -ef | grep pmon | grep %s"%(args["dbname"])
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
			par=open("%sexport_%s_%s_%s.par"%(args["par_dir"],args["schema"],args["runner"],TS), "w+")
			par.write("userid='/ as sysdba'\n")
			par.write("schemas=%s\n"%(args["schema"]))
			par.write("dumpfile=%s_%s_%s.dmp\n"%(args["schema"],args["runner"],TS))
			par.write("logfile=%s_%s_%s.log\n"%(args["schema"],args["runner"],TS))
			par.write("directory=%s"%(args["directory"]))
			par.close()
			par_read=open("%sexport_%s_%s_%s.par"%(args["par_dir"],args["schema"],args["runner"],TS),"r+")
			par_content=par_read.read()
			print(par_content)
			par_read.close()
			par_name="export_%s_%s_%s.par"%(args["schema"],args["runner"],TS)
			print(par_name)
		except:
			print("par file creation unscuccessful")

		try:
			#getting absolute path ofr .par file
			par_path=os.path.join(os.getcwd(),"%s"%(par_name))			
	
			#creating .sh file to set environment variables and start db schema backup
			export=open("%sexport_%s.sh"%(args["par_dir"],TS),"w+")
			export.write(". /home/oracle/scripts/oracle_env_%s.sh\nexpdp parfile=%sexport_%s_%s_%s.par"%(args["dbname"],args["par_dir"],args["schema"],args["runner"],TS))
			
			export.close()
			export_content="%sexport_%s.sh"%(args["par_dir"],TS)	
			os.popen("chmod 700 %s"%(export_content))
		except:
			print("%s file creation failed"%(export_content))

		try:
			#start DB schema backup using expdp command
			print("Starting Schema export for %s"%(args["schema"]))
			subprocess.call(['sh',"%s"%(export_content)])		
		except:
				print("expdp backup failed")

		#opening log file in read mode
		with open(exportlog_path,'r') as exportlog:
			exportlog_contents=exportlog.read()
		
		#checking for "successfully completed" string in export_log
		if "successfully completed" in  exportlog_contents:
			print("expdp backup successful")
			status="success"
		else:
			print("expdp backup failed")	
			status="failure"
	
		try:	
			G_zipp(file_dir=exportdmp_path)

			STATUS="COMPLETED"
			db_connection(schema_pass=args["schema_pass"],schema=args["schema"],OP_ID=OP_ID,OP_NAME=OP_NAME,OP_TYPE=OP_TYPE,RUNNER=args["runner"],STATUS=STATUS,dbname=args["dbname"])
		except:
			print("Zipping of %s was unsuccessful!"%(export_dmp)) 	
			STATUS="ERROR"
			db_connection(schema_pass=args["schema_pass"],schema=args["schema"],OP_ID=OP_ID,OP_NAME=OP_NAME,OP_TYPE=OP_TYPE,RUNNER=args["runner"],STATUS=STATUS,dbname=args["dbname"])
		return status	
	else:
		print("Database is not running")

def backup_f_d(**args):
	OP_ID=4
	OP_NAME="File/Directory Copy"
	OP_TYPE="BACKUP"
	
	dest_dir="%s/%s/%s/"%(args["dst"],args["runner"],TS)
	dest_path=os.path.join(os.getcwd(),dest_dir)
	

	STATUS="RUNNING"
	db_connection(schema_pass=args["schema_pass"],schema=args["schema"],OP_ID=OP_ID,OP_NAME=OP_NAME,OP_TYPE=OP_TYPE,RUNNER=args["runner"],STATUS=STATUS,dbname=args["dbname"])

	#creating directory path if it doesnt exist yet
	os.makedirs(dest_path, exist_ok=True)	
	if os.path.isdir(args["src"]):
		try:
			#priting to  stdout
			print("Copying source directory %s to %s"%(args["src"],dest_path))
      	#using shutil copytree to copy a directory and its contents to destination dir
			shutil.copytree(args["src"],dest_path)
			status="success"
			STATUS="COMPLETED"
			db_connection(schema_pass=args["schema_pass"],schema=args["schema"],OP_ID=OP_ID,OP_NAME=OP_NAME,OP_TYPE=OP_TYPE,RUNNER=args["runner"],STATUS=STATUS,dbname=args["dbname"])
		except:
			print("Copying of source directory %s to %s failed"%(a,dest_path))
			status="failure"
			STATUS="ERROR"
			db_connection(schema_pass=args["schema_pass"],schema=args["schema"],OP_ID=OP_ID,OP_NAME=OP_NAME,OP_TYPE=OP_TYPE,RUNNER=args["runner"],STATUS=STATUS,dbname=args["dbname"])
	elif os.path.isfile(args["src"]):
		try:
    		#printing to stdout
			print("Copying source file %s to %s"%(args["src"],dest_path))

      	#using shutil copy function to copy src to dst
			shutil.copy(args["src"],dest_path)

      	#printing to stdout
			print("Copy complete!")
			status="success"
			STATUS="COMPLETED"
			db_connection(schema_pass=args["schema_pass"],schema=args["schema"],OP_ID=OP_ID,OP_NAME=OP_NAME,OP_TYPE=OP_TYPE,RUNNER=args["runner"],STATUS=STATUS,dbname=args["dbname"])
		except:
			print("Copying of source file %s to %s has failed")
			status="failure"
			STATUS="ERROR"
			db_connection(schema_pass=args["schema_pass"],schema=args["schema"],OP_ID=OP_ID,OP_NAME=OP_NAME,OP_TYPE=OP_TYPE,RUNNER=args["runner"],STATUS=STATUS,dbname=args["dbname"])
			

	return status

def disk_utilization_check(**args):
	OP_ID=5
	OP_NAME="DISK MONITORING"
	OP_TYPE="MONITORING"
		
	try:
		STATUS="RUNNING"
		db_connection(schema_pass=args["schema_pass"],schema=args["schema"],OP_ID=OP_ID,OP_NAME=OP_NAME,OP_TYPE=OP_TYPE,RUNNER=args["runner"],STATUS=STATUS,dbname=args["dbname"])
		while True:
			
			disk_util=int(subprocess.getoutput(("df -h|grep '%s'|awk '{print $4}'|sed 's/%%//g'"%(args["disk"]))))
			if disk_util > 52 :
				print("WARNING:%s has crossed a critical threshold of 52%%"%(args["disk"]))
				time.sleep(60)
			elif disk_util >= 50:
				print("WARNING:%s has crossed threshold of 50%%"%(args["disk"]))
				time.sleep(300)
			elif disk_util < 50:
				print("%s is within threshold"%(args["disk"]))
				status="success"
				time.sleep(5)	
		return status
	except KeyboardInterrupt:
		print("\nKeyboard Interrupt Detected!")
		STATUS="COMPLETED"
		db_connection(schema_pass=args["schema_pass"],schema=args["schema"],OP_ID=OP_ID,OP_NAME=OP_NAME,OP_TYPE=OP_TYPE,RUNNER=args["runner"],STATUS=STATUS,dbname=args["dbname"])
	except ValueError:
		print("invalid literal for int() with base 10: %s"%(args["threshold"]))
				
def G_zipp(**args):
	file_name=os.path.basename(args["file_dir"])
	
	#checking if the source is a file 
	if os.path.isfile(args["file_dir"]):
		try:
			#constructing output file name
			tar_file="%s_%s.tgz"%(args["file_dir"],TS)
			#opening tar archive in write mode with gzip conmpression
			with tarfile.open(tar_file,'w:gz') as tar:
				#adding the source file to tar archive with the same base name
				tar.add(args["file_dir"],arcname=os.path.basename(args["file_dir"]))
				
				print("%s has been succcessfully Gzipped!"%(file_name))
				status="success"
		except:
			print("%s has failed to zip"%(file_name))
			status="failure"
	elif os.path.isdir(args["file_dir"]):
		try:
			#constructing output file name
			tar_dir="%s_%s.tgz"%(args["file_dir"],TS)
			# opens a tar archive with gzip compression in write mode
			with tarfile.open(tar_dir, "w:gz") as tar:
				#adding source file to tar archive under source file name
				tar.add(args["file_dir"],arcname=os.path.basename(args["file_dir"]))

				print("%s has been successfully Gzipped!"%(file_name))						
				status="success"
		except:
			print("%s has failed to zip"%(file_name))
			status="failure"
	#returning status to caller
	return status

def unzipp(**args):
	try:
		#opens specified tar archive
		file=tarfile.open(args["file_dir"])
		print(file.getnames())
		
		#extracts the content of the tar archive to the destination path
		file.extractall(args["destination"])
		
		#close tar archive
		file.close()	
		print("%s a has successfully been unzipped!"%(args["file_dir"]))
	except:
		print("%s has failed to unzip!"%(args["file_dir"]))
	
def database_import(**args):
	OP_ID=2
	OP_NAME="IMPORT"
	OP_TYPE="BACKUP"
	STATUS="RUNNING"
	db_connection(schema_pass=args["schema_pass"],schema=args["schema"],OP_ID=OP_ID,OP_NAME=OP_NAME,OP_TYPE=OP_TYPE,RUNNER=args["runner"],STATUS=STATUS,dbname=args["connect_db"])
	
	#variable declaration	
	dblog_path="%sdb_status.log"%(args["par_dir"])
	import_log="%s_%s_%s.log"%(args["schema"],args["import_schema"],TS)
	importlog_path=os.path.join(args["sourcedb_physical"],import_log)
	
	#removes the .tgz extenstion from the dumpfile and extracts the basename
	dmpfile_path=os.path.splitext(args["dmp_file"])[0]	
	dmp_base=os.path.basename(dmpfile_path)
	
	#removes time stamp from .dmp file
	index_dmp=dmp_base.find('.dmp')
	dumpfile_strip=dmp_base[:index_dmp + 4] if index_dmp != -1 else dmp_base	
	

	#calling unzip function to unzip zipped dmp file
	unzipp(file_dir=args["dmp_file"],destination=args["sourcedb_physical"])
	
	try:
		#creating .par file for import
		par=open("impdp_%s_%s_%s.par"%(args["schema"],args["import_schema"],TS),'w+')				
		par.write("userid='/ as sysdba'\n")
		par.write("schemas=%s\n"%(args["schema"]))
		par.write("remap_schema=%s:%s_%s_imported\n"%(args["schema"],args["schema"],args["import_schema"]))
		par.write("dumpfile=%s\n"%(dumpfile_strip))
		par.write("logfile=%s_%s_%s.log\n"%(args["schema"],args["import_schema"],TS))
		par.write("directory=%s\n"%(args["directory"]))
		par.write("table_exists_action=replace")
		par.close()
	
		par_read=open("%simpdp_%s_%s_%s.par"%(args["par_dir"],args["schema"],args["import_schema"],TS),'r+')
		par_content=par_read.read()
		print(par_content)
	
		par_name="impdp_%s_%s_%s.par"%(args["schema"],args["import_schema"],TS)
		print(par_name)
	except Exception as e:
		print("Par file creation unsuccessful: %s"%(e))
			
	try:
		#creating.sh file for import
		import_exec=open("%simport_exec.sh"%(args["par_dir"]), "w+")
		import_exec.write(". /home/oracle/scripts/oracle_env_%s.sh\nimpdp parfile=impdp_%s_%s_%s.par"%(args["dbname"],args["schema"],args["import_schema"],TS))
		import_exec.close()
		import_content=("%simport_exec.sh"%(args["par_dir"]))
		os.popen("chmod 700 %s"%(import_content))
	except Exception as e:
		print(".sh file creation failed: %s"%(e))
		
	#Checking DB status
	subprocess.call(['sh', '%sdblogin.sh'%(args["par_dir"])])

	try:
		#opening db_status.log file in read mode
		with open(dblog_path,'r') as dblog:
			dblog_contents=dblog.read()

			#checking if "OPEN" string is present in the file contents
			if "OPEN" in dblog_contents:
				print("Database is Open!")
			else:
				print("Database is not Open!")
				sys.exit()
	except FileNotFoundError as e:
		print("File not found: %s"%(e))
	
	#Starting import
	subprocess.call(['sh', '%simport_exec.sh'%(args["par_dir"])])
	
	try:
		#opening log file in read mode
		with open(importlog_path,'r') as importlog:
			importlog_contents=importlog.read()
		
		#checking for "completed" string in import_log
		if "completed" in  importlog_contents:
			print("impdp import successful")
			status="success"
			STATUS="COMPLETED"
			db_connection(schema_pass=args["schema_pass"],schema=args["schema"],OP_ID=OP_ID,OP_NAME=OP_NAME,OP_TYPE=OP_TYPE,RUNNER=args["runner"],STATUS=STATUS,dbname=args["connect_db"])
		else:
			print("import failed")
			status="failure"
	except FileNotFoundError as e:
		print("File not found: %s"%(e))
		status="failure"
		STATUS="ERROR"
		db_connection(schema_pass=args["schema_pass"],schema=args["schema"],OP_ID=OP_ID,OP_NAME=OP_NAME,OP_TYPE=OP_TYPE,RUNNER=args["runner"],STATUS=STATUS,dbname=args["connect_db"])
	return status


def data_migration(**args):	
	OP_ID=3
	OP_TYPE="MIGRATION"
	OP_NAME="DATA_MIGRATION"
	connect_db=args["source_dbname"]

	#setting status and calling db_connection function with required arguments	
	STATUS="RUNNING"
	db_connection(schema_pass=args["schema_pass"],schema=args["schema"],OP_ID=OP_ID,OP_NAME=OP_NAME,OP_TYPE=OP_TYPE,RUNNER=args["runner"],STATUS=STATUS,dbname=args["source_dbname"])
	
	try:
		#calling database backup function with required arguments
		database_backup(schema_pass=args["schema_pass"],schema=args["schema"],runner=args["runner"],directory=args["directory"],par_dir=args["par_dir"],sourcedb_physical=args["sourcedb_physical"],dbname=args["source_dbname"])
			
		#absolute path to dmp file
		sourcedmp_path="%s%s_%s_%s.dmp_%s.tgz"%(args["sourcedb_physical"],args["schema"],args["runner"],TS,TS)
		
      #calling database import function to import exported schema into database
		database_import(connect_db=connect_db,schema_pass=args["schema_pass"],schema=args["schema"],runner=args["runner"],directory=args["directory"],par_dir=args["par_dir"],sourcedb_physical=args["importdb_physical"],dbname=args["target_dbname"],import_schema=args["import_schema"],dmp_file=sourcedmp_path)
		status="successful"

		#setting status then calling db_connection function with required arguments
		STATUS="COMPLETED"
		db_connection(schema_pass=args["schema_pass"],schema=args["schema"],OP_ID=OP_ID,OP_NAME=OP_NAME,OP_TYPE=OP_TYPE,RUNNER=args["runner"],STATUS=STATUS,dbname=args["source_dbname"])
	except:
		print("Data Migration for %s into %s was unsuccessful"%(args["schema"],args["importdb_physical"]))
		status="failure"
			
		#setting status and calling db_connection function with required arguments
		STATUS='ERROR'
		db_connection(schema_pass=args["schema_pass"],schema=args["schema"],OP_ID=OP_ID,OP_NAME=OP_NAME,OP_TYPE=OP_TYPE,RUNNER=args["runner"],STATUS=STATUS,dbname=args["source_dbname"])
		return status

def db_connection(**args):
	#variable declaration
	OP_ID=args["OP_ID"]
	OP_NAME=args["OP_NAME"]
	OP_TYPE=args["OP_TYPE"]
	RUNNER=args["RUNNER"]
	STATUS=args["STATUS"]

	#formatting timestamp to format of timestamp in database
	current_TS=time.strftime('%d-%b-%y %I.%M.%S.000000 %p')	
	
	#checking if status passed is equal to RUNNING, COMPLETED OR ERROR
	if STATUS == "RUNNING":
	
		connection=cx_Oracle.connect(user=args["schema"], password=args["schema_pass"], dsn="MKIT-DEV-OEM/%s"%(args["dbname"]))	
		print(connection.version)
		cursor = connection.cursor()
	
		cursor.execute("""insert into operations values(:OP_ID_INS,:OP_NAME_INS,:OP_STARTTIME_INS,:OP_ENDTIME_INS,:RUNNER_INS,:STATUS_INS,:OP_TYPE_INS)""",	
		OP_ID_INS=OP_ID,
		OP_NAME_INS=OP_NAME,
		OP_STARTTIME_INS=current_TS,
		OP_ENDTIME_INS=current_TS,
		RUNNER_INS=RUNNER,
		STATUS_INS=STATUS,
		OP_TYPE_INS=OP_TYPE)
	

		connection.commit()
	elif STATUS == "COMPLETED":
		connection=cx_Oracle.connect(user=args["schema"], password=args["schema_pass"], dsn="MKIT-DEV-OEM/%s"%(args["dbname"]))
		print(connection.version)
		cursor = connection.cursor()
	
		cursor.execute("""UPDATE operations 
							SET OP_ENDTIME = :OP_ENDTIME_UPDATE, STATUS ='COMPLETED'
							WHERE STATUS = 'RUNNING' AND RUNNER = :RUNNER_INS
							""",
													
		OP_ENDTIME_UPDATE=current_TS,
		RUNNER_INS=RUNNER)
		
		connection.commit()
	elif STATUS == "ERROR":
		connection=cx_Oracle.connect(user=args["schema"], password=args["schema_pass"], dsn="MKIT-DEV-OEM/%s"%(args["dbname"]))
		print(connection.version)
		cursor = connection.cursor()

		cursor.execute("""UPDATE operations
               		SET OP_ENDTIME = :OP_ENDTIME_UPDATE, STATUS ='ERROR'
               		WHERE STATUS = 'RUNNING' AND RUNNER = :RUNNER_INS
               		""",

		OP_ENDTIME_UPDATE=current_TS,
		RUNNER_INS=RUNNER)

		connection.commit()








