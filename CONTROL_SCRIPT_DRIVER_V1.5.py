#!/usr/bin/python



#imported modules
import stack_modules_v5 as k
import sys



#variable declaration

comlin_args=len(sys.argv) -1

#main body


if sys.argv[1] == "database_backup":
	if comlin_args == 6:
		schema=sys.argv[2]
		runner=sys.argv[3]
		directory=sys.argv[4]
		par_dir=sys.argv[5]
		sourcedb_physical=sys.argv[6]
		
		#calling database backup fucntion with required arguments
		k.database_backup(schema,runner,directory,par_dir,sourcedb_physical)
	elif comlin_args != 6:
		print()
		print("Incorrect arguments")
		print("USAGE: the following is how to properly use the database_backup function!")
		print()
		print("       database_backup")
		print("       eg .modulename database_backup schema runner directory par_dir sourcedb_physical")	
		print()
elif sys.argv[1] == "backup_f_d":
	if comlin_args == 4:
		src=sys.argv[2]
		dst=sys.argv[3]
		runner=sys.argv[4]				
		#calling file directory copy function with required arguments
		k.backup_f_d(src,dst,runner)
	elif comlin_args != 4:
		print()
		print("Incorrect arguments")
		print("USAGE: the following is how to properly use the backup_f_d function!")
		print()
		print("       backup_f_d")
		print("       eg .modulename backup_f_d src dst runner")	
		print()
else:
	print()
	print("Function not defined or incorrect arguments")
	print()
	print("USAGE: the following is how to properly use the database_backup, and backup_f_d function!")
	print()
	print("       database_backup")
	print("       eg .modulename database_backup schema runner directory par_dir sourcedb_physical")
	print()
	print("       backup_f_d")
	print("       eg .modulename backup_f_d src dst runner")
	print()

