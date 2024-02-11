#!/usr/bin/python



#imported modules
import sys
import stack_modules_v15 as k



#variable declaration

comlin_args=len(sys.argv) -1

#main body

#condition for if no command line arguments are entered at run time
if comlin_args == 0:
	print()
	function=input("what task are you trying to do? database_backup, backup_f_d, disk_utilization_check, G_zipp, unzipp, database_import, data_migration?: ").lower()	
	if function == "database_backup":
	 
		#prompting user for required arguments to call database backup function
		schema=input("Enter Schemas: ")
		runner=input("Enter Runner: ")
		directory=input("Enter Directory: ")
		par_dir=input("Enter path for .par file creation: ")
		sourcedb_physical=input("Enter source DB physical path: ")
		dbname=input("Enter target database name: ")
		schema_pass=input("Enter password to schema to log activity: ")
		
		email_send=input("would you like to send an email upon completion? Yes or No: ").lower()
		if email_send == "yes":
			email_add=input("enter email: ")
		
			#calling database backup fucntion with required arguments
			status=k.database_backup(schema_pass=schema_pass,schema=schema,runner=runner,directory=directory,par_dir=par_dir,sourcedb_physical=sourcedb_physical,dbname=dbname)
			
			#calling STACK EMAIL function with required arguments
			k.STACK_EMAIL(email_add=email_add,status=status,function=function,runner=runner)
		elif email_send == "no":
			k.database_backup(schema_pass=schema_pass,schema=schema,runner=runner,directory=directory,par_dir=par_dir,sourcedb_physical=sourcedb_physical,dbname=dbname)
		else:
			print("Incorrect Option Entered!")
			print("Please Enter Yes or No!")	
	elif function == "backup_f_d":
		#prompting user for required arguments to call backup_f_d function
		src=input("Enter source path: ")
		dst=input("Enter destination path: ")
		runner=input("Enter runner: ")
		schema=input("Enter schema to log Operation activity in: ")
		dbname=input("Enter database name to log activity in: ")
		schema_pass=input("Enter password to schema to log activity: ")

		#prompting user for email to be sent	
		email_send=input("would you like to send an email upon completion? Yes or No: ").lower()
		if email_send == "yes":
			email_add=input("enter email: ")
	
			#calling file directory copy function with required arguments
			status=k.backup_f_d(schema_pass=schema_pass,dbname=dbname,schema=schema,src=src,dst=dst,runner=runner)	
			k.STACK_EMAIL(email_add=email_add,status=status,function=function,runner=runner)
		elif email_send == "no":
			k.backup_f_d(schema_pass=schema_pass,dbname=dbname,schema=schema,src=src,dst=dst,runner=runner)
		else:
			print("Incorrect Option Entered!")
			print("Please Enter yes or no!")

	elif function == "disk_utilization_check":
		disk=input("Enter disk: ")
		threshold=int(input("Enter Threshold: "))
		schema_pass=input("Enter password to schema to log activity: ")
		schema=input("Enter schema to log Operation activity in: ")
		runner=input("Enter runner: ")
		dbname=input("Enter database name to log activity in: ")

		email_send=input("would you like to send an email upon completion? Yes or No: ").lower()
		if email_send == "yes":
			email_add=input("enter email: ")
			
			#assigning disk util check function call the status variable
			status=k.disk_utilization_check(dbname=dbname,runner=runner,schema=schema,schema_pass=schema_pass,disk=disk,threshold=threshold)
			k.STACK_EMAIL(disk=disk,email_add=email_add,status=status,function=function,runner=runner)
		
		elif email_send == "no":
			k.disk_utilization_check(dbname=dbname,runner=runner,schema=schema,schema_pass=schema_pass,disk=disk,threshold=threshold)
		else:
			print("Incorrect Option Entered!")
			print("Please Enter Yes or No!")	

	elif function == "G_zipp":
		file_dir=input("Enter absolute path of file or directory that you would like to G_zipp: ")
	
		
		email_send=input("would you like to send an email upon completion? Yes or No: ").lower()
		if email_send == "yes":
			email_add=input("enter email: ")
			runner=input("Enter runner: ")
				
			#calling G_zipp function with required arguments
			status=k.G_zipp(file_dir=file_dir)
			
			k.STACK_EMAIL(email_add=email_add,status=status,function=function,runner=runner)
		elif email_send == "no":
			k.G_zipp(file_dir=file_dir)
		else:
			print("Incorrect Option Entered!")
			print("Please Enter Yes or No!")
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
		schema_pass=input("Enter password to schema to log activity: ")
		connect_db=input("Enter database name to log activity in: ")
		
		#prompting for email address
		email_send=input("would you like to send an email upon completion? Yes or No: ").lower()
		if email_send == "yes":
			email_add=input("enter email: ")
	
			#calling database backup import with required arguments
			status=k.database_import(connect_db=connect_db,schema_pass=schema_pass,schema=schema,directory=directory,par_dir=par_dir,sourcedb_physical=sourcedb_physical,dbname=dbname,import_schema=import_schema,dmp_file=dmp_file,runner=runner)
				
			#calling email function with required arguments
			k.STACK_EMAIL(email_add=email_add,status=status,function=function,runner=runner)
		elif email_send == "no":
			#calling database import function with required arguments
			k.database_import(connect_db=connect_db,schema_pass=schema_pass,runner=runner,schema=schema,directory=directory,par_dir=par_dir,sourcedb_physical=sourcedb_physical,dbname=dbname,import_schema=import_schema,dmp_file=dmp_file)
		else:
			print("Incorrect Option Entered!")
			print("Please Enter Yes or No!")

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
		schema_pass=input("Enter password to schema to log activity: ")		

		#prompting for email_address
		email_send=input("would you like to send an email upon completion? Yes or No: ").lower()
		
		if email_send == "yes":
			email_add=input("enter email: ")
			
			status=k.data_migration(schema_pass=schema_pass,schema=schema,runner=runner,directory=directory,sourcedb_physical=sourcedb_physical,par_dir=par_dir,importdb_physical=importdb_physical,source_dbname=source_dbname,target_dbname=target_dbname,import_schema=import_schema)
			#calling stack email function with required arguments
			k.STACK_EMAIL(email_add=email_add,status=status,function=function,runner=runner)
		elif email_send == "no":
			#calling data_migration function
			k.data_migration(schema_pass=schema_pass,schema=schema,runner=runner,directory=directory,sourcedb_physical=sourcedb_physical,par_dir=par_dir,importdb_physical=importdb_physical,source_dbname=source_dbname,target_dbname=target_dbname,import_schema=import_schema)	
		else:
			print("Incorrect Option Entered!")
			print("Please Enter Yes or No!")
			
	else:
		print("Function not defined")
		print()
		print("USAGE: the following is how to properly use the database_backup, and backup_f_d function!")
		print()
		print("       database_backup")
		print("       eg .modulename database_backup schema runner directory par_dir sourcedb_physical dbname schema_pass")
		print()
		print("       backup_f_d")
		print("       eg .modulename backup_f_d src dst runner schema dbname schema_pass")
		print()	
		print("       disk_utilization_check")
		print("       eg .modulename disk_utilization_check disk threshold schema runner dbname")
		print()
		print("       G_zipp")
		print("       eg .modulename G_zipp file_dir")
		print()
		print("       unzipp")
		print("       eg .modulename unzipp file_dir")
		print()
		print("       database_import")
		print("       eg .modulename database_backup schema directory par_dir sourcedb_physical dbname import_schema dmp_file runner schema_pass")
		print()
		print("       data_migration")
		print("       eg .modulename data_migration schema runner directory par_dir sourcedb_physical ,importdb_physical source_dbname target_dbname import_schema schema_pass")
		

elif sys.argv[1] == "database_backup":
	if comlin_args == 8:
		schema=sys.argv[2]
		runner=sys.argv[3]
		directory=sys.argv[4]
		par_dir=sys.argv[5]
		sourcedb_physical=sys.argv[6]
		dbname=sys.argv[7]
		schema_pass=sys.argv[8]
	
		#calling database backup fucntion with required arguments
		k.database_backup(schema_pass=schema_pass,schema=schema,runner=runner,directory=directory,par_dir=par_dir,sourcedb_physical=sourcedb_physical,dbname=dbname)
	elif comlin_args == 9:
		schema=sys.argv[2]
		runner=sys.argv[3]
		directory=sys.argv[4]
		par_dir=sys.argv[5]
		sourcedb_physical=sys.argv[6]
		dbname=sys.argv[7]
		schema_pass=sys.argv[8]
		email_add=sys.argv[9]

		#calling database backup fucntion with required arguments
		status=k.database_backup(schema_pass=schema_pass,schema=schema,runner=runner,directory=directory,par_dir=par_dir,sourcedb_physical=sourcedb_physical,dbname=dbname)
		k.STACK_EMAIL(email_add=email_add,status=status,function=sys.argv[1],runner=runner)
	
	elif comlin_args != 8 and comlin_args != 9:
		print()
		print("Incorrect arguments")
		print("USAGE: the following is how to properly use the database_backup function!")
		print()
		print("       database_backup")
		print("       eg .modulename database_backup schema runner directory par_dir sourcedb_physical dbname schema_pass")	
		print()
		print("       database_backup:EMAIL")
		print("       eg .modulename database_backup schema runner directory par_dir sourcedb_physical dbname schema_pass email_add")
		print()
elif sys.argv[1] == "backup_f_d":
	if comlin_args == 7:
		src=sys.argv[2]
		dst=sys.argv[3]
		runner=sys.argv[4]
		schema=sys.argv[5]
		dbname=sys.argv[6]
		schema_pass=sys.argv[7]
				
		#calling file directory copy function with required arguments
		k.backup_f_d(src=src,dst=dst,runner=runner,schema=schema,dbname=dbname,schema_pass=schema_pass)
	elif comlin_args == 8:
		src=sys.argv[2]
		dst=sys.argv[3]
		runner=sys.argv[4]
		schema=sys.argv[5]
		dbname=sys.argv[6]
		schema_pass=sys.argv[7]
		email_add=sys.argv[8]
		
		#calling file directory copy function with required arguments
		status=k.backup_f_d(src=src,dst=dst,runner=runner,schema=schema,dbname=dbname,schema_pass=schema_pass)
		k.STACK_EMAIL(email_add=email_add,status=status,function=sys.argv[1],runner=runner)	
	elif comlin_args != 7 and comlin_args != 8:
		print()
		print("Incorrect arguments")
		print("USAGE: the following is how to properly use the backup_f_d function!")
		print()
		print("       backup_f_d")
		print("       eg .modulename backup_f_d src dst runner schema dbname schema_pass")	
		print()
		print("       backup_f_d:EMAIL")
		print("       eg .modulename backup_f_d src dst runner schema dbaname schema_pass email_add")
		print()
elif sys.argv[1] == "disk_utilization_check":
	if comlin_args == 7:
		disk=sys.argv[2]
		threshold=int(sys.argv[3])
		schema_pass=sys.argv[4]
		schema=sys.argv[5]
		runner=sys.argv[6]
		dbname=sys.argv[7]
			
		#calling unzip function with required argument
		k.disk_utilization_check(disk=disk,threshold=threshold,schema_pass=schema_pass,schema=schema,runner=runner,dbname=dbname)
	elif comlin_args == 8:
		disk=sys.argv[2]
		threshold=int(sys.argv[3])
		schema_pass=sys.argv[4]
		schema=sys.argv[5]
		runner=sys.argv[6]
		dbname=sys.argv[7]
		email_add=sys.argv[8]

		#calling unzip function with required argument
		status=k.disk_utilization_check(disk=disk,threshold=threshold,schema_pass=schema_pass,schema=schema,runner=runner,dbname=dbname)
		k.STACK_EMAIL(email_add=email_add,status=status,function=sys.argv[1],runner=runner)

	elif comlin_args != 7 and comlin_args != 8:
		print()
		print("Incorrect arguments")
		print("USAGE: the following is how to properly use the disk_utilization_check function!")
		print()
		print("       disk_utilization_check")
		print("       eg .modulename disk_utilization_check disk threshold schema_pass schema runner dbname")
		print()
		print("       disk_utilization_check:EMAIL")
		print("       eg .modulename disk_utilization_check disk threshold schema_pass schema runner dbname email_add ")
		print()	
elif sys.argv[1] == "G_zipp":
	if comlin_args == 2:
		file_dir=sys.argv[2]

		#calling unzip function with required argument
		k.G_zipp(file_dir=file_dir)
	elif comlin_args == 4:
		file_dir=sys.argv[2]
		email_add=sys.argv[3]
		runner=sys.argv[4]
		
		#calling unzip function with required argument
		status=k.G_zipp(file_dir=file_dir)
		k.STACK_EMAIL(email_add=email_add,status=status,function=sys.argv[1],runner=runner)
	elif comlin_args != 2 and comlin_args != 4:
		print()
		print("Incorrect arguments")
		print("USAGE: the following is how to properly use the disk_utilization_check function!")
		print()
		print("       G_zipp")
		print("       eg .modulename G_zipp file_dir")
		print()
		print("       G_zipp:EMAIL")
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
		print("USAGE: the following is how to properly use the disk_utilization_check function!")
		print()
		print("       unzipp")
		print("       eg .modulename unzipp file_dir")
		print()
elif sys.argv[1] == "database_import":
	if comlin_args == 10:
		schema=sys.argv[2]
		directory=sys.argv[3]
		par_dir=sys.argv[4]
		sourcedb_physical=sys.argv[5]
		dbname=sys.argv[6]
		import_schema=sys.argv[7]
		dmp_file=sys.argv[8]
		schema_pass=sys.argv[10]
		
		#calling database import function with required argument
		k.database_import(schema_pass=schema_pass,schema=schema,directory=directory,par_dir=par_dir,sourcedb_physical=sourcedb_physical,dbname=dbname,import_schema=import_schema,dmp_file=dmp_file)
	elif comlin_args == 11:
		schema=sys.argv[2]
		runner=sys.argv[3]
		directory=sys.argv[4]
		par_dir=sys.argv[5]
		sourcedb_physical=sys.argv[6]
		dbname=sys.argv[7]
		import_schema=sys.argv[8]
		dmp_file=sys.argv[9]
		schema_pass=sys.argv[10]
		email_add=sys.argv[11]
		
		status=k.database_import(schema=schema,runner=runner,directory=directory,par_dir=par_dir,sourcedb_physical=sourcedb_physical,dbname=dbname,import_schema=import_schema,dmp_file=dmp_file)
		
		k.STACK_EMAIL(email_add=email_add,status=status,function=sys.argv[1],runner=runner)
	elif comlin_args != 10 and comlin_args != 11:
		print()
		print("Incorrect arguments")
		print("USAGE: the following is how to properly use the database_import function!")
		print()
		print("       database_import")
		print("       eg .modulename database_import schema directory par_dir sourcedb_physical dbname import_schema dmp_file schema_pass")
		print()
		print("       database_import:EMAIL")
		print("       eg .modulename database_import schema runner directory par_dir sourcedb_physical dbname import_schema dmp_file schema_pass email_add")
		print()

elif sys.argv[1] == "data_migration":
	if comlin_args == 11:
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

		#calling data_migration function with required arguments	
		k.data_migration(schema_pass=schema_pass,schema=schema,runner=runner,directory=directory,sourcedb_physical=sourcedb_physical,par_dir=par_dir,importdb_physical=importdb_physical,source_dbname=source_dbname,target_dbname=target_dbname,import_schema=import_schema)
	elif comlin_args == 12:
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
		email_add=sys.argv[12]
		
		#calling data_migration function with required arguments
		status=k.data_migration(schema_pass=schema_pass,schema=schema,runner=runner,directory=directory,sourcedb_physical=sourcedb_physical,par_dir=par_dir,importdb_physical=importdb_physical,source_dbname=source_dbname,target_dbname=target_dbname,import_schema=import_schema)
			
		#calling STACK_EMAIL function with required arguments
		k.STACK_EMAIL(email_add=email_add,status=status,function=sys.argv[1],runner=runner)

	elif comlin_args != 11 and comlin_args != 12:
		print()
		print("Incorrect arguments")
		print("USAGE: the following is how to properly use the database_import function!")
		print()
		print("       database_migration")
		print("       eg .modulename database_migration schema runner directory par_dir sourcedb_physical ,importdb_physical source_dbname target_dbname import_schema schema_pass")
		print()
		print("       data_migration:EMAIL")
		print("       eg .modulename data_migration schema runner directory par_dir sourcedb_physical ,importdb_physical source_dbname target_dbname import_schema schema_pass email_add")
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
	print("       database_backup:EMAIL")
	print("       eg .modulename database_backup schema runner directory par_dir sourcedb_physical dbname schema_pass email_add")
	print()
	print("       backup_f_d")
	print("       eg .modulename backup_f_d src dst runner schema dbaname schema_pass")
	print()
	print("       backup_f_d:EMAIL")
	print("       eg .modulename backup_f_d src dst runner schema dbaname schema_pass email_add")
	print()
	print("       disk_utilization_check")
	print("       eg .modulename disk_utilization_check disk threshold schema_pass schema runner dbname")
	print()
	print("       disk_utilization_check:EMAIL")
	print("       eg .modulename disk_utilization_check disk threshold schema_pass schema runner dbname email_add ")
	print()
	print("       G_zipp")
	print("       eg .modulename G_zipp file_dir")
	print()
	print("       G_zipp:EMAIL")
	print("       eg .modulename G_zipp file_dir email_add runner")
	print()
	print("       unzipp")
	print("       eg .modulename unzipp file_dir")
	print()
	print("       database_import")
	print("       eg .modulename database_import schema runner directory par_dir sourcedb_physical dbname import_schema dmp_file schema_pass")
	print()
	print("       database_import:EMAIL")
	print("       eg .modulename database_import schema runner directory par_dir sourcedb_physical dbname import_schema dmp_file schema_pass email_add")
	print()
	print("       database_migration")
	print("       eg .modulename database_migration schema runner directory par_dir sourcedb_physical ,importdb_physical source_dbname target_dbname import_schema schema_pass")
	print()
	print("       data_migration:EMAIL")
	print("       eg .modulename data_migration schema runner directory par_dir sourcedb_physical ,importdb_physical source_dbname target_dbname import_schema schema_pass email_add")




