# Question: Write a program to find least of 8 numbers enetered by the user.

a1 = int(input("Enter 1st number: "))
a2 = int(input("Enter 2nd number: "))
a3 = int(input("Enter 3rd number: "))
a4 = int(input("Enter 4th number: "))
a5 = int(input("Enter 5th number: "))
a6 = int(input("Enter 6th number: "))
a7 = int(input("Enter 7th number: "))
a8 = int(input("Enter 8th number: "))

if(a1<a2):
    v1 = a1
else:
    v1= a2

if(a3<a4):
    v2 = a3
else:
    v2 = a4

if(a5<a6):
    v3 = a5
else:
    v3 = a6

if(a7<a8):
    v4 = a7
else:
    v4 = a8

if(v1<v2):
    w = v1
else:
    w = v2

if(v3<v4):
    x = v3
else:
    x = v4

if(w<x):
    print("The least number is " + str(w))
else:
    print("The least number is "+ str(x))
