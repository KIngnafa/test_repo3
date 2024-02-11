#!/usr/bin/python



#imported modules
import sys
import stack_modules_v8 as k



#variable declaration

comlin_args=len(sys.argv) -1

#main body

#condition for if no command line arguments are entered at run time
if comlin_args == 0:
	print()
	function=input("what task are you trying to do? database_backup, backup_f_d, disk_utilization_check or G_zipp?: ")
	
	if function == "database_backup":
		#prompting user for required arguments to call database backup function
		schema=input("Enter Schemas: ")
		runner=input("Enter Runner: ")
		directory=input("Enter Directory: ")
		par_dir=input("Enter path for .par file creation: ")
		sourcedb_physical=input("Enter source DB physical path: ")
		dbname=input("Enter target database name: ")
		
		#calling database backup fucntion with required arguments
		k.database_backup(schema,runner,directory,par_dir,sourcedb_physical,dbname)

	elif function == "backup_f_d":
		#prompting user for required arguments to call backup_f_d function
		src=input("Enter source path: ")
		dst=input("Enter destination path: ")
		runner=input("Enter runner: ")
	
		#calling file directory copy function with required arguments
		k.backup_f_d(src,dst,runner)
	
	elif function == "disk_utilization_check":
		disk=input("Enter disk: ")
		threshold=int(input("Enter Threshold: "))
	
		k.disk_utilization_check(disk,threshold)
	elif function == "G_zipp":
		file_dir=input("Enter absolute path of file or directory that you would like to G_zipp: ")
		
		#calling G_zipp function with required arguments
		k.G_zipp(file_dir)
	else:
		print("Function not defined")
		print()
		print("USAGE: the following is how to properly use the database_backup, backup_f_d, disk_utilization_check and G_zipp function!")
		print()
		print("       database_backup")
		print("       eg .modulename database_backup schema runner directory par_dir sourcedb_physical dbaname")
		print()
		print("       backup_f_d")
		print("       eg .modulename backup_f_d src dst runner")
		print()	
		print("       disk_utilization_check")
		print("       eg .modulename disk_utilization_check disk threshold")
		print()
		print("       G_zipp")
		print("       eg .modulename G_zipp file_dir")
		print()

elif sys.argv[1] == "database_backup":
	if comlin_args == 6:
		schema=sys.argv[2]
		runner=sys.argv[3]
		directory=sys.argv[4]
		par_dir=sys.argv[5]
		sourcedb_physical=sys.argv[6]
		dbname=sys.argv[7]
		
		#calling database backup fucntion with required arguments
		k.database_backup(schema,runner,directory,par_dir,sourcedb_physical,dbname)
	elif comlin_args != 6:
		print()
		print("Incorrect arguments")
		print("USAGE: the following is how to properly use the database_backup function!")
		print()
		print("       database_backup")
		print("       eg .modulename database_backup schema runner directory par_dir sourcedb_physical dbname")	
		print()
elif sys.argv[1] == "backup_f_d":
	if comlin_args == 4:
		src=sys.argv[2]
		dst=sys.argv[3]
		runner=sys.argv[4]				
		#calling file directory copy function with required arguments
		k.file_directory(src,dst,runner)
	elif comlin_args != 4:
		print()
		print("Incorrect arguments")
		print("USAGE: the following is how to properly use the backup_f_d function!")
		print()
		print("       backup_f_d")
		print("       eg .modulename backup_f_d src dst runner")	
		print()
elif sys.argv[1] == "disk_utilization_check":
	if comlin_args == 3:
		disk=sys.argv[2]
		threshold=int(sys.argv[3])
		
		k.disk_utilization_check(disk,threshold)
	elif comlin_args != 3:
		print()
		print("Incorrect arguments")
		print("USAGE: the following is how to properly use the disk_utilization_check function!")
		print()
		print("       disk_utilization_check")
		print("       eg .modulename disk_utilization_check disk  threshold")
		print()	
elif sys.argv[1] == "G_zipp":
	if comlin_args == 2:
		file_dir=sys.argv[2]
	
		k.G_zipp(file_dir)
	elif comlin_args != 2:
		print()
		print("Incorrect arguments")
		print("USAGE: the following is how to properly use the G_zipp function!")
		print()
		print("       G_zipp")
		print("       eg .modulename G_zipp file_dir")
		print()
else:
	print()
	print("Function not defined or incorrect arguments")
	print()
	print("USAGE: the following is how to properly use the database_backup, backup_f_d, disk_utilization_check and G_zipp function!")
	print()
	print("       database_backup")
	print("       eg .modulename database_backup schema runner directory par_dir sourcedb_physical dbname")
	print()
	print("       backup_f_d")
	print("       eg .modulename backup_f_d src dst runner")
	print()
	print("       disk_utilization_check")
	print("       eg .modulename disk_utilization_check disk  threshold")
	print()
	print("       G_zipp")
	print("       eg .modulename G_zipp file_dir")
	print()
