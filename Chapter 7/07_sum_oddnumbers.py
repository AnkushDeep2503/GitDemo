n = int(input("Enter: "))

i = 0
sum = 0
while(i<=n):
    sum = sum + i
    i = (i + 2)-1
    print(sum, i)
print(sum)