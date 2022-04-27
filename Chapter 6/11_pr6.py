# Question: Write a program to find whether a given username contains less than 10 characcters or not.

username = input("Enter the username: ")

a = len(username)

if(a<10):
    print("Username has less than 10 characters")
else:
    print("Username has more than 10 characters")
