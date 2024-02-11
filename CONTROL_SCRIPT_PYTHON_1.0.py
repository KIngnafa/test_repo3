#!/usr/bin/python

#imported modules
import shutil
import os



#variable declaration
src="/home/oracle/scripts/practicedir_ynr_sep23/backupdir"
dst="/home/oracle/scripts/practicedir_ynr_sep23/testpythondir/"

#main body 

if __name__ == "__main__":

	if os.path.isdir(src):
		#priting to  stdout
		print("Copying source directory %s to %s"%(src,dst))
		#using shutil copytree to copy a directory and its contents to destination dir
		shutil.copytree(src,dst)
	else:
		#printing to stdout
		print("Copying source file %s to %s"%(src,dst))
	
		#using shutil copy function to copy src to dst
		shutil.copy(src,dst)
	
		#printing to stdout
		print("Copy complete!")
	

	
