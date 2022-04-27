a = "Society"
print (a[0:6]) #This is repeated in the case of List also.
# Note: 0:3 means 0,1 and 2 (4th position of index, i,e 3 is not counted)
b = "Surbhi"
print(b[0:-1])
# This is called string slicing. The index in a string starts from 0 to (length -1)
c = "Noida"
print(c[ :4]) # is same as 0:4 (first index number)
print(c[0: ]) # is same as 0:5 (last index number)

# Negative indices: for Noida: from backside it is counted. a is -1, d is -2, i is -3, o is -4, N is -5.
d ="Noida"
print(d[-5:-1]) # is same as 0:4