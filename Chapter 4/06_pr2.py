# Question: Write a program to accept marks of 6 students and display them in a sorted manner.

m1 = int(input("Enter the marks of student1: "))
m2 = int(input("Enter the marks of student2: "))
m3 = int(input("Enter the marks of student3: "))
m4 = int(input("Enter the marks of student4: "))
m5 = int(input("Enter the marks of student5: "))
m6 = int(input("Enter the marks of student6: "))

marksofstudents = [m1, m2, m3, m4, m5, m6]
print(marksofstudents)
marksofstudents.sort()
print(marksofstudents)
marksofstudents.append(100)
print(marksofstudents)
marksofstudents.pop(2) #deleted the 3rd index value (0, 1, 2)
print(marksofstudents)
i = int(input("Enter the value of element in 4th position: "))
marksofstudents.insert(3,i )
print(marksofstudents)

