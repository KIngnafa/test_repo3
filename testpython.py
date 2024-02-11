#!/usr/bin/python


"""
#put double quotes in a string
txt="Wilson said \"I like Python!\" and i think he means it."
print(txt)


#capitalize
name="wilson"
print(name.capitalize())


#len function
names=["wilson", "yinka", "leke"]
print(len(names))

#pop,insert,del,remove,append
names=["Wilson", "Yinka", "Leke", "Rob", "Sam", "ola"]
names.append("Mike")
names.insert(1, "Saks")
a=names.insert(3, "Nick")
names.remove("Leke")
names.pop()
names.pop(0)
del names[0]
b=len(names)
print(names)
print(b)

#clear function
print("Clearing the list")
names.clear()
print(names)

#join 2 lists
names=["Wilson", "Yinka", "Leke", "Rob", "Sam", "ola"]
names2=["Dam", "Jack", "Remi"]
#names3=names+names2
#print(names3)

#join 2 lists together with for loop
for x in names2:
	names.append(x)
print(names)

#extend to join 2 lists together
names=["Wilson", "Yinka", "Leke", "Rob", "Sam", "ola"]
names2=["Dam", "Jack", "Remi"]
names.extend(names2)
print(names)


#put names in a list
names=list(("Wilson", "Yinka", "Leke", "Rob", "Sam", "ola"))
print(names)


#counts how many number are in the list
numbers=[1,1,2,2,3,4,5,6,6,7,8,9,9,10]
a=len(numbers)
print(a)

#find out which numbers are duplicates
duplicates={}

numbers=[1,1,2,2,3,4,5,6,6,7,8,9,9,10]
#num_result=set(numbers)



#how to identify duplicates
for x in numbers:
	#print(x)
	if x not in duplicates:
		duplicates[x] = 1
		#print(duplicates)
		#duplicates.append(x)
		#print(x)
	else:
		duplicates[x] += 1
		#print("This is not a duplicate")

for x in numbers:
	
#set
#dup=[1,1,2,2,3,4,5,6,6,7,8,9,9,10]
#depp=set(dup)
#print(depp)

"""
"""
#dictionaries
cars={
	"Brand":"Dodge",
	"Model":"Hellcat",
	"year": 2023
}

print(cars["Brand"])

print(cars.get("Model"))

#changing value of a key
cars["year"]=2024
print(cars)


cars={
   "Brand":"Dodge",
   "Model":"Hellcat",
   "year": 2023
}

#printing everything in the dictionary
for x in cars:
	print(x)
#printing just values
for x in cars:
	print(cars[x])

#prints values in dictionary
for x in cars.values():
	print(x)

#printing keys and values with .items
for x,y in cars.items():
	print(x,"=>", y)



cars={
   "Brand":"Dodge",
   "Model":"Hellcat",
   "year": 2023
}

#checking if key is in dictionary
if "Brand" in cars:
	print("Brand Exist in the cars dictionary")
print(len(cars))


#adding key and value to dictionary
cars["Tag"]="Q23ED56Y"
print(cars)


#deletes key and value from dictionary
cars.pop("Tag")
print(cars)


cars["Tag"]="Q23ED56Y"

#delete dictionary with popitem
cars.popitem()
print(cars)



#del
cars={
   "Brand":"Dodge",
   "Model":"Hellcat",
   "year": 2023
}

del cars["year"]
print(cars)

#del cars
#print(cars)

#using clear to clear a dictionary
cars.clear()
print(cars)


cars={
   "Brand":"Dodge",
   "Model":"Hellcat",
   "year": 2023
}

#copies the car dictionary into cars2
cars2=cars.copy()
print(cars2)

#dict copies a dictionary
cars3=dict(cars)
print(cars3)




#nested dictionary
car1={
	"Brand":"Dodge",
	"Model":"Hellcat",
	"year": 2023
}

cars2={
	"Brand":"Toyota",
	"Model":"Camry",
	"year": 2021
}


cars3={
	"Brand":"Honda",
	"Model":"Accord",
	"year": 2024
}


cars = {
	"car1": car1,
	"car2": cars2,
	"cars3": cars3
}

#print(cars["car1"]) 
print(cars)



name="Michael"

if name == "Michael":
	pass


i=1

while i < 6:
	print(i)
	i += 1


counter = 1
while counter < 6:
	print(counter)
	if counter == 3:
		break
	counter += 1



counter = 0

while counter <= 10:
	print(counter)
	if counter == 11:
		break
	counter += 1


empty_list=[]

while 2 > 1:
	i=int(input("Enter a number: "))
	empty_list.append(i)
	
	if i == 0:
		break
print(empty_list)

import os

while 6 > 2:
	file_name=os.path.exists("/home/oracle/scripts/practicedir_wil_sep23/testloop.txt")
	
	if file_name == "true":
		break
	else:
		i=input("Looking for testloop.txt: ")

		if i == os.path.exists("/home/oracle/scripts/practicedir_wil_sep23/testloop.txt"):
		break

import os
import subprocess

while 6 > 2:
	print("Seaching for file \"testloop.txt\"")

	if os.path.exists("/home/oracle/scripts/practicedir_wil_sep23/testloop.txt"):

		print("File now exists")
		output=subprocess.getoutput("ls -ltr /home/oracle/scripts/practicedir_wil_sep23/testloop.txt") 
		
		print(output)
		break


i=1
while i < 6:
	i += 1
	if i == 3:
		continue
	print(i)



i=1
while i < 6:
	print(i)
	i += 1
else:
	print("i is no longer less than 6")
"""












	





