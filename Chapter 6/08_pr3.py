# Question: Write a program to find out whether a student is pass or fail, if it requires total 40% and atleast 33% in each subject to pass.
# Assume 3 subjects and take marks as an input from the user.

sub1 = int(input("Enter marks for subject 1: "))
sub2 = int(input("Enter marks for subject 2: "))
sub3 = int(input("Enter marks for subject 3: "))


totalsubject = (sub1 + sub2 + sub3)/3

if(sub1<33 or sub2<33 or sub3<33):
    print("failed")

elif(totalsubject<40):
    print("Sorry, you are failed")

else:
    print("You have passed successfully")