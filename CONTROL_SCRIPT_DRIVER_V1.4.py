#!/usr/bin/python



#imported modules
import stack_modules_v4 as k
import sys





#function declaration








comlin_args=len(sys.argv) -1
#main body
if comlin_args == 5:
	
	schema=sys.argv[1]
	runner=sys.argv[2]
	directory=sys.argv[3]
	par_dir=sys.argv[4]
	sourcedb_physical=sys.argv[5]		
	
	#calling database backup function with required arguments
	k.database_backup(schema,runner,directory,par_dir,sourcedb_physical)

	

elif comlin_args == 3:
	src=sys.argv[1]
	dst=sys.argv[2]
	runner=sys.argv[3]

	#calling backup_f_d function with required arguments
	k.backup_f_d(src,dst,runner)
