#!/usr/bin/python

#imported modules
import shutil
import os
import sys


#variable declaration
src=sys.argv[1]
dst=sys.argv[2]

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
	

	
