a = set()
print(type(a))

a.add(4)
a.add(6) # adding single element in the empty set
a.add(7)
a.add(4)
a.add(7)
a.add("Ankush")
a.add(4.321)
a.add((1,2,3, 4, 4)) #tuple can be added in set #any immutable object can be added #repeatative intigers can be present in tuple however.
print(a)
print(len(a)) #counts number of elements in the set
a.remove(4) #removes the element 4 from set
print(a)
print(len(a))
