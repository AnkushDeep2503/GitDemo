# Question: Write a program to find out whether a student is pass or fail, if it requires total 40% and atleast 33% in each subject to pass.
# Assume 3 subjects and take marks as an input from the user.

sub1 = int(input("Print the marks for sub1: "))
sub2 = int(input("Print the marks for sub2: "))
sub3 = int(input("Print the marks for sub3: "))

total = (sub1 + sub2 + sub3)/3

if(sub1<33 or sub2<33 or sub3<3):
    print("The student has failed")

elif(total<40):
    print("The student has failed and has not met the criteria")

else:
    print("student has passed")