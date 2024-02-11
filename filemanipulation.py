#!/usr/bim/python
import os
"""
user_entry=input("Please Enter first name: ")

print("user entered : {}".format(user_entry))

print(type(user_entry))


for x in range(2,10):
	print(x)


#increment
for x in range(2,10,2):
	print(x)



#creating/writing into a file
fo=open("test_rasheed.par","w+")
#print("The name of the file is {}".format(fo.name))
#print("is {} closed? {} ".format(fo.name,fo.closed))
fo.write("userid='/ as sysdba;'\nschemas=stack_temp\ndumpfile=stack_temp.dmp\nlogfile=stack_temp.log\ndirectory=DATA_PUMP_DIR")
fo.close()
#print("is {} closed? {} ".format(fo.name,fo.closed))

#opening and reading from a file
file_read=open("/home/oracle/scripts/test_rasheed.par","r+")
file_content=file_read.read()
print(file_content)
file_read.close()
"""


dir_content=os.listdir('.')
print(dir_content)
