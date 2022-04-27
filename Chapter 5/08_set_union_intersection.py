a = {200, 300, 600, 900, 500}
b = {300, 400, 600, 1000, 700}
print(a.union(b)) #displays all the elements in both sets (not repeatative)
print(a.intersection(b)) #displays common elements of both sets
print(a-b)
print(b-a)

c={'s','v','a','d'}
d={1,6,3,0,5}
c.update(d)
d.update()
print(c)
print(d)