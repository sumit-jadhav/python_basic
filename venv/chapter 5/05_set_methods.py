
b=set()

print(type(b))
b.add(4)
b.add(5)
b.add(5) #adding a value repetedly doesnot change the set
b.add((4,5,6))# cannot add list and dictonary in the set
b.add(9)
print(b)

print(len(b))#length of the set

b.remove(5)#remove the given value
print(b)

print(b.pop())
print(b)