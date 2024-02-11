#!/usr/bin/python



#imported modules
import sys
import stack_modules_v17 as k
import getpass as w


#variable declaration

comlin_args=len(sys.argv) -1

#main body

#condition for if no command line arguments are entered at run time
if comlin_args == 0:
	print()
	function=input("what task are you trying to do? database_backup, backup_f_d, disk_utilization_check, G_zipp, unzipp, database_import, data_migration, aws_create_user?: ").lower()	
	if function == "database_backup":
	 
		#prompting user for required arguments to call database backup function
		schema=input("Enter Schemas: ")
		runner=input("Enter Runner: ")
		directory=input("Enter Directory: ")
		par_dir=input("Enter path for .par file creation: ")
		sourcedb_physical=input("Enter source DB physical path: ")
		dbname=input("Enter target database name: ")
		user=input("Enter username to log database activity: ")
		schema_pass=w.getpass(prompt="Enter password to schema to log activity: ", stream=None)
		DSN=input("Enter DSN: ")
		
		#calling database backup fucntion with required arguments
		k.database_backup(DSN=DSN,user=user,schema_pass=schema_pass,schema=schema,runner=runner,directory=directory,par_dir=par_dir,sourcedb_physical=sourcedb_physical,dbname=dbname)
	
	elif function == "backup_f_d":
		#prompting user for required arguments to call backup_f_d function
		src=input("Enter source path: ")
		dst=input("Enter destination path: ")
		runner=input("Enter runner: ")
		dbname=input("Enter database name to log activity in: ")
		user=input("Enter username to log database activity: ")
		schema_pass=w.getpass(prompt="Enter password to schema to log activity: ", stream=None)
		DSN=input("Enter DSN: ")
		
		#calling file directory copy function with required arguments
		k.backup_f_d(DSN=DSN,user=user,schema_pass=schema_pass,dbname=dbname,src=src,dst=dst,runner=runner)	

	elif function == "disk_utilization_check":
		disk=input("Enter disk: ")
		threshold=int(input("Enter Threshold: "))
		user=input("Enter username to log database activity")
		schema_pass=w.getpass(prompt="Enter password to schema to log activity: ", stream=None)
		runner=input("Enter runner: ")
		dbname=input("Enter database name to log activity in: ")
		DSN=input("Enter DSN: ")
			
		#assigning disk util check function call the status variable
		k.disk_utilization_check(DSN=DSN,user=user,dbname=dbname,runner=runner,schema_pass=schema_pass,disk=disk,threshold=threshold)
		
	elif function == "G_zipp":
		file_dir=input("Enter absolute path of file or directory that you would like to G_zipp: ")
		runner=input("Enter runner: ")
				
		#calling G_zipp function with required arguments
		k.G_zipp(file_dir=file_dir)
	
	elif function == "unzipp":
		file_dir=input("Enter absolute path of file or directory that you would like to unzipp: ")
		destination=input("Enter Destination path: ")	
		
		#calling unzipp function with required arguments
		k.unzipp(file_dir=file_dir,destination=destination)
	
	elif function == "database_import":
		#prompting for variable required for a database import
		schema=input("Enter Schemas: ")
		directory=input("Enter Directory: ")
		par_dir=input("Enter path for .par file creation: ")	
		sourcedb_physical=input("Enter source DB physical path: ")
		dbname=input("Enter database name to Import Schema into: ")
		import_schema=input("Enter schema to import to Database: ")
		dmp_file=input("Enter path absolute path to Zipped dump file: ")
		runner=input("Enter Runner: ")
		user=input("Enter username to log database activity: ")
		schema_pass=w.getpass(prompt="Enter password to schema to log activity: ", stream=None)
		DSN=input("Enter database name to log activity in: ")
	
		#calling database backup import with required arguments
		k.database_import(DSN=DSN,user=user,schema_pass=schema_pass,schema=schema,directory=directory,par_dir=par_dir,sourcedb_physical=sourcedb_physical,dbname=dbname,import_schema=import_schema,dmp_file=dmp_file,runner=runner)
				
	elif function == "data_migration":
		schema=input("Enter Schemas: ")
		runner=input("Enter runner name: ")
		directory=input("Enter Directory: ")
		par_dir=input("Enter .par dir: ")
		sourcedb_physical=input("Enter source DB physical path: ")
		importdb_physical=input("Enter destination DB physical path: ")
		source_dbname=input("Enter source database name to export from: ")
		target_dbname=input("Enter target database name to Import Schema into: ")
		import_schema=input("Enter schema name to import to Database: ")
		user=input("Enter username to log database activity: ")
		schema_pass=w.getpass(prompt="Enter password to schema to log activity: ", stream=None)
		DSN=input("Enter database name to log activity in: ")
		
		#calling database import function with required arguments	
		k.data_migration(DSN=DSN,user=user,schema_pass=schema_pass,schema=schema,runner=runner,directory=directory,sourcedb_physical=sourcedb_physical,par_dir=par_dir,importdb_physical=importdb_physical,source_dbname=source_dbname,target_dbname=target_dbname,import_schema=import_schema)
			
	elif function == "aws_create_user":
		service=input("Enter Service: ")
		user=input("Enter User to create: ")
		
		k.aws_create_user(service=service,user=user)
		
	else:
		print("Function not defined")
		print()
		print("USAGE: the following is how to properly use the database_backup, and backup_f_d function!")
		print()
		print("       database_backup")
		print("       eg .modulename database_backup schema runner directory par_dir sourcedb_physical dbname user schema_pass DSN")
		print()
		print("       backup_f_d")
		print("       eg .modulename backup_f_d src dst runner dbname schema_pass user DSN")
		print()	
		print("       disk_utilization_check")
		print("       eg .modulename disk_utilization_check disk threshold runner dbname user DSN")
		print()
		print("       G_zipp")
		print("       eg .modulename G_zipp file_dir")
		print()
		print("       unzipp")
		print("       eg .modulename unzipp file_dir")
		print()
		print("       database_import")
		print("       eg .modulename database_backup schema directory par_dir sourcedb_physical dbname import_schema dmp_file runner schema_pass user DSN")
		print()
		print("       data_migration")
		print("       eg .modulename data_migration schema runner directory par_dir sourcedb_physical ,importdb_physical source_dbname target_dbname import_schema schema_pass user DSN")
		

elif sys.argv[1] == "database_backup":
	if comlin_args == 11:
		schema=sys.argv[2]
		runner=sys.argv[3]
		directory=sys.argv[4]
		par_dir=sys.argv[5]
		sourcedb_physical=sys.argv[6]
		dbname=sys.argv[7]
		user=sys.argv[8]
		schema_pass=sys.argv[9]
		DSN=sys.argv[10]
		#calling database backup fucntion with required arguments
		k.database_backup(DSN=DSN,schema_pass=schema_pass,schema=schema,runner=runner,directory=directory,par_dir=par_dir,sourcedb_physical=sourcedb_physical,dbname=dbname)
	
	elif comlin_args != 11:
		print()
		print("Incorrect arguments")
		print("USAGE: the following is how to properly use the database_backup function!")
		print("       eg .modulename database_backup schema runner directory par_dir sourcedb_physical dbname user schema_pass DSN")
		print()

elif sys.argv[1] == "backup_f_d":
	if comlin_args == 11:
		src=sys.argv[2]
		dst=sys.argv[3]
		runner=sys.argv[4]
		dbname=sys.argv[5]
		schema_pass=sys.argv[8]		
		user=sys.argv[9]
		DSN=sys.argv[10]
		
		#calling file directory copy function with required arguments
		k.backup_f_d(src=src,dst=dst,runner=runner,dbname=dbname,schema_pass=schema_pass,user=user,DSN=DSN)
	elif comlin_args != 11:
		print()
		print("Incorrect arguments")
		print("USAGE: the following is how to properly use the backup_f_d function!")
		print()
		print("       backup_f_d")
		print("       eg .modulename backup_f_d src dst runner schema dbname schema_pass user DSN")	
		print()
elif sys.argv[1] == "disk_utilization_check":
	if comlin_args == 9:
		disk=sys.argv[2]
		threshold=int(sys.argv[3])
		schema_pass=sys.argv[4]
		runner=sys.argv[5]
		dbname=sys.argv[6]
		user=sys.argv[7]
		DSN=sys.argv[8]	
		email_add=sys.argv[9]		
		#calling unzip function with required argument
		k.disk_utilization_check(disk=disk,threshold=threshold,schema_pass=schema_pass,schema=schema,runner=runner,dbname=dbname)

	elif comlin_args != 9:
		print()
		print("Incorrect arguments")
		print("USAGE: the following is how to properly use the disk_utilization_check function!")
		print()
		print("       disk_utilization_check")
		print("       eg .modulename disk_utilization_check disk threshold schema_pass runner dbname user DSN email_add")
		print()
elif sys.argv[1] == "G_zipp":
	if comlin_args == 4:
		file_dir=sys.argv[2]
		
		#calling unzip function with required argument
		k.G_zipp(file_dir=file_dir)
	elif comlin_args != 4:
		print()
		print("Incorrect arguments")
		print("USAGE: the following is how to properly use the G_zipp function!")
		print()
		print("       G_zipp")
		print("       eg .modulename G_zipp file_dir email_add runner")
		print()
elif sys.argv[1] == "unzipp":
	if comlin_args == 2:
		file_dir=sys.argv[2]

		#calling unzip function with required argument
		k.unzipp(file_dir=file_dir)
	elif comlin_args != 2:
		print()
		print("Incorrect arguments")
		print("USAGE: the following is how to properly use the unzipp function!")
		print()
		print("       unzipp")
		print("       eg .modulename unzipp file_dir")
		print()
elif sys.argv[1] == "database_import":
	if comlin_args == 12:
		schema=sys.argv[2]
		directory=sys.argv[3]
		par_dir=sys.argv[4]
		sourcedb_physical=sys.argv[5]
		dbname=sys.argv[6]
		import_schema=sys.argv[7]
		dmp_file=sys.argv[8]
		schema_pass=sys.argv[9]
		user=sys.argv[10]
		DSN=sys.argv[11]
		
		#calling database import function with required argument
		k.database_import(user=user,schema_passs=schema_pass,email_add=email_add,schema=schema,runner=runner,directory=directory,par_dir=par_dir,sourcedb_physical=sourcedb_physical,dbname=dbname,import_schema=import_schema,dmp_file=dmp_file)

	elif comlin_args != 12:
		print()
		print("Incorrect arguments")
		print("USAGE: the following is how to properly use the database_import function!")
		print()
		print("       database_import")
		print("       eg .modulename database_import schema directory par_dir sourcedb_physical dbname import_schema dmp_file schema_pass user DSN email_add")
		print()

elif sys.argv[1] == "data_migration":
	if comlin_args == 13:
		#setting variables
		schema=sys.argv[2]	
		runner=sys.argv[3]
		directory=sys.argv[4]
		par_dir=sys.argv[5]
		sourcedb_physical=sys.argv[6]	
		importdb_physical=sys.argv[7]
		source_dbname=sys.argv[8]
		target_dbname=sys.argv[9]
		import_schema=sys.argv[10]
		schema_pass=sys.argv[11]
		user=sys.argv[12]
		DSN=sys.argv[13]
		
		#calling data_migration function with required arguments
		k.data_migration(DSN=DSN,user=user,schema_pass=schema_pass,schema=schema,runner=runner,directory=directory,sourcedb_physical=sourcedb_physical,par_dir=par_dir,importdb_physical=importdb_physical,source_dbname=source_dbname,target_dbname=target_dbname,import_schema=import_schema)	

	elif comlin_args != 13:
		print()
		print("Incorrect arguments")
		print("USAGE: the following is how to properly use the database_import function!")
		print()
		print("       data_migration")
		print("       eg .modulename database_migration schema runner directory par_dir sourcedb_physical ,importdb_physical source_dbname target_dbname import_schema schema_pass user DSN")
		print()

else:
	print()
	print("Function not defined or incorrect arguments")
	print()
	print("USAGE: the following is how to properly use this module!")
	print()
	print("       database_backup")
	print("       eg .modulename database_backup schema runner directory par_dir sourcedb_physical dbname schema_pass")
	print()
	print("       backup_f_d")
	print("       eg .modulename backup_f_d src dst runner schema dbname schema_pass user DSN email_add")
	print()
	print("       disk_utilization_check")
	print("       eg .modulename disk_utilization_check disk threshold schema_pass schema runner dbname user DSN email_add")
	print()
	print("       G_zipp")
	print("       eg .modulename G_zipp file_dir email_add")
	print()
	print("       unzipp")
	print("       eg .modulename unzipp file_dir")
	print()
	print("       database_import")
	print("       eg .modulename database_import schema directory par_dir sourcedb_physical dbname import_schema dmp_file schema_pass user DSN email_add")
	print()
	print("       database_migration")
	print("       eg .modulename database_migration schema runner directory par_dir sourcedb_physical ,importdb_physical source_dbname target_dbname import_schema schema_pass user DSN email_add")



