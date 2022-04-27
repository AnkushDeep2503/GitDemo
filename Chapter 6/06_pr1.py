# Question: Write a program to find greatest of 4 numbers enetered by the user.

a1 = int(input("Enter 1st number: "))
a2 = int(input("Enter 2nd number: "))
a3 = int(input("Enter 3rd number: "))
a4 = int(input("Enter 4th number: "))

if(a1>a4):
    b = a1
else:
    b = a4

if(a2>a3):
    c = a2
else:
    c = a3

if(b>c):
    print(type("Greatest number is " + str(b)))
else:
    print(type("Greatest number is " + str(c)))

    