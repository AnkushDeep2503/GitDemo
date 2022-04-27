# Question: Write a program to find out whether a given name is present in a list or not.

name = input("Enter the name:\n ")

l = ["ankush", "computer", "234", "james bond"]

if(name in l):
    print("The name is present")

else:
    print("The name is not present in the list")
