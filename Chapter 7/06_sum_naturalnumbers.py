# Question: Find the sum of natural numbers till n.

n = int(input("Enter the number\n: "))

i = 1
sum = 0
while(i<=n):
    print(sum, i)
    sum = sum + i
    i = i+1
print("Sum of Natural Numbers: ", sum)
