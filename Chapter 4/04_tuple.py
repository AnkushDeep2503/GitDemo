t = (1, 2, 4, 7, 5, 4, 3, 6, 12, 5, 1, 5, 5, 5)
print(t[2])
# a[2]=3 #Tuple cannot be changed so it is called immutable.
# t1 = () #Emplty Tuple
# print(t1)
t3 = (3,) #single element must have comma at the end of the element
print(t3)
print(t.index(4)) # shows element number from index, not the index number of elements
print(t.count(5)) # shows the number of times 5 has appeared in the tuple