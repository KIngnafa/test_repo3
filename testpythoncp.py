#!/bin/usr/python

#len
'''
a="Yinka"
name=len(a)

print("the length of %s is %s"%(a,name))

#strip
b="Yinka"
print(b.strip("a"))


threshold='65% '

if int(threshold.strip('% ')) < 70:
	print("threshold is less than 70")
else:
	print("threshold is not less than 70")

#upper lower
b="yINkA"
upper=b.upper()
lower=b.lower()
print("My name in uppercase is %s"%(upper))
print("My name in lowercase is %s"%(lower))

#replace
a="Stack"

print(a.replace('S','C'))

threshold="65%"

if int(threshold.replace('%','')) < 70:
	print("threshold is less than 70")

name="Yinka"

print(name.replace("Yinka","Yemi"))

file=open("test1replace.txt",'w+')
file.write("baseball")
file.close()

file_content=open("test1replace.txt",'r+')
file_content=file_content.read()
print("replacing the output")
print(file_content.replace("baseball","basketball"))

final=open("test1replace.txt",'w+')
final.write(file_content.replace("baseball","basketball"))
final.close()

final_content=open("test1replace.txt",'r+')
final_read=final_content.read()
print("writing changes into file")
print(final_read)


#split
name="Yinka Rasheed"

token=name.split(' ')

print(token)

print(token[1])

disks="/u01,/u02,/u03,/u04,/u05,/backup"

token=disks.split(',')


if token[5].strip("/") == "backup":
	print("index 5 is backup")
else:
	print("index 5 is not backup")

#count
txt="Stack IT Training students stack up aloy of bread."
if "bread" in txt:
	print("bread exists in the statement")

txt="Stack IT Training students stack up alot of bread."

if "Stack" in txt:
	cnt=txt.lower().count("stack")
	print("Stack appears %s times"%(cnt))


#arbituary arguments
def my_function(*names):
	print("The youngest child is " + names[2])

my_function("John", "Jeff", "Rachel")
	
def calculator(*num):
	x=num[0]+num[1]
	print(x)
calculator(1,2)

#keyword arguments
def my_function(name3,name1,name2):
	print("My name is " + name1)

my_function(name1="Yinka",name3="Yemi",name2="Kyle")
	
def my_function(**names):
	print("Yinka's last name is " + names["lname"])


my_function(fname="Yinka",lname="Rasheed")

def addition(**num):
	add=int(num["num1"]) + int(num["num2"])
	print(add)
def subtraction(**num):
	sub=int(num["num1"]) - int(num["num1"])
	print(sub)
def multiply(**num):
	mul=int(num["num1"]) * int(num["num1"])
	print(mul)


func=input("what would you like to do addition, subtraction, or multiply?: ")

if func == "addition":
	number1=input("Enter your first number: ")
	number2=input("Enter your second number: ")
	
	addition(num1=number1, num2=number2)
elif func == "subtraction":
	number1=input("Enter your first number: ")
	number2=input("Enter your second number: ")

	add(num1=number1, num2=number2)
elif func == "multiply":
	number1=input("Enter your first number: ")
	number2=input("Enter your second number: ")		

	multiply(num1=number1, num2=number2)





		










