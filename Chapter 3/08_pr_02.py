# Question: Write a program to fill in a letter template given below with name and date.
# letter = Dear </name/>
# you are selected!
# </date/>

# name = input("Enter a name")
# date = input("Enter a date")
# print("Dear, " + name + "!"+ "\nYou are selected!\n" + date)

letter = '''Dear <|NAME|>,
You are Selected!

Date: <|Date|>'''

name = input("Enter your Name\n")
Date = input("Enter Date\n")

letter = letter.replace("<|NAME|>", name)
letter = letter.replace("<|Date|>", Date)

print(letter)

