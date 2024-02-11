#!/usr/bin/python

"""
names=["Myles","Mike","Charles","Yinka","Nick","Ola"]
names2=["Kyle","Yemi","Allister","Missy","Akeem","Esterlyn"]

names3=names+names2

priint(names3)

names=["Myles","Mike","Charles","Yinka","Nick","Ola"]
names2=["Kyle","Yemi","Allister","Missy","Akeem","Esterlyn"]

for x in names2:
	names.append(x)

print(names)

names=["Myles","Mike","Charles","Yinka","Nick","Ola"]
names2=["Kyle","Yemi","Allister","Missy","Akeem","Esterlyn"]

names.extend(names2)
print(names)

names=list(("Myles","Mike","Charles","Yinka","Nick","Ola"))
print(names)

numbers=[1,1,2,2,3,4,5,6,6,7,8,9,9,10]

num_dup=set(numbers)
print(num_dup)
#set
#dup=[1,1,2,2,3,4,5,6,6,7,8,9,9,10]
#print(depp)

"""
numbers=[1,1,2,2,3,4,5,6,6,7,8,9,9,10]
duplicates={}


for x in numbers:
	if x not in duplicates:
		duplicates[x]=1
	else:
		duplicates[x] += 1

print(duplicates)
