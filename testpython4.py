#!/usr/bin/python


import os
import subprocess
"""
txt="Yinka said \"I Like python!\" and i think he means it."
print(txt)


name="yinka"
print(name.capitalize())

names=["wilson", "yinka", "leke"]
print(len(names))

names=["wilson", "yinka", "leke", "Rob", "Sam", "Ola"]
names.append("mike")
names.insert(1,"saks")
a=names.insert(3,"nick")
names.remove("leke")
names.pop()
names.pop(0)
del names[0]

b=len(names)
print(names)
print(b)


print("Clearing the list")
names.clear()
print(names)

names=["wilson", "yinka", "leke", "Rob", "Sam", "Ola"]
names2=["Dam", "Jack", "Remi"]
names3=names+names2
#print(names3)


for x in names2:
	names.append(x)
print(names)



cars={
	"Brand":"Honda",
	"Model":"Accord",
	"Year": 2010
}

del cars["Year"]
print(cars)


cars.clear()
print(cars)

cars.clear()
print(cars)

cars={
   "Brand":"Honda",
   "Model":"Accord",
   "Year": 2010
}

cars2=cars.copy()
print(cars2)


cars3=dict(cars)
print(cars3)

car1 = {
	"Brand":"Honda",
	"Model":"Accord",
	"Year": 2010
}
car2 = {
	"Brand":"Toyota",
	"Model":"Camry",
	"Year": 2005
}
car3 = {
   "Brand":"Hyundai",
   "Model":"santa",
   "Year": 2023		
}


cars = {
	"car1": car1,
	"car2": car2,
	"car3": car3,
}
print(cars["car1"])

#pass
name="Michael"

if name == "Michael":
	pass

#while loops
i=1

while i < 6:
	print(i)
	#increment by 1
	i += 1

counter = 1
while i < 6:
	print(i)
	if i == 3:
		break
	i += 1

counter = 0
while counter <= 10:
   print(counter)
   if counter == 11:
      break
   counter += 1

#infinite while loop
emptylist = []

while 2 > 1:
	num=int(input("Input a number or something: "))
	emptylist.append(num)
	if num == 0:
		break
print(emptylist)


file="/home/oracle/scripts/practicedir_ynr_sep23/testloop.txt"
while True:
	print("Looking for file testloop.txt")
	if os.path.exists(file):
		print("testloop.txt exists!")
		list=subprocess.getoutput("ls -ltr %s"%(file))
		print(list)
		break

i=1
while i < 6:
	i += 1
	if i == 3:
		continue
	print(i)	

#while loop else:
i=1

while i < 6:
	print(i)
	i += 1
else:
	print("i is no longer less than 6")
"""







