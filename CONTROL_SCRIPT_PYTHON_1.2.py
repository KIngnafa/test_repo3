#!/usr/bin/python

#imported modules
import shutil
import os
import sys


#function declaration
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
src=sys.argv[1]
dst=sys.argv[2]

#main body 

if __name__ == "__main__":
	file_directory_cp(src,dst)	

	
