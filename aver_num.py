#!/usr/bin/python


mysum = 0
num =int(input("Enter the number of num :"))
for i in range(num):
    value= int(input("Give me number :"))
    mysum+=value

myavg = mysum/num
print("avg  = %d" % (myavg))
