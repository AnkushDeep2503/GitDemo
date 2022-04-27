def func(name,age):
    print("Hello beautiful your name is " + name + " and your age is "+ age)

i = 0
while i<4:
    name = input("Enter the name\n")
    age = input("Enter age\n")
    func(name, age)
    i = i+1
print("End of Loop")