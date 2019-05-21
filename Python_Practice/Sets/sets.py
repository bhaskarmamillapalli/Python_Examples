#! /usr/bin/python

a =set ([1,2,3,4,5])
#print("printing values of set %s"%a)
print(a)
print("priting values of set{}".format(a))
print("print values of set ::%s"%a)

#update the set values.
a.update(set([1,2,3,4,5,6]))
print("updated set values",a)

a.intersection_update(set([4,5,6,7]))
print("Intersection values",a)

#remove and discard functions

a.remove(6)
print(a)

#this will return error if  the element is not available in the set.
#a.remove(7)
#print("removing the 7th element",a)

#this does not return error like remove.
a.discard(7)
print("removing the 7th element",a)

#to remove an arbitrary element from the set.
print("Pop function",a.pop())
print("printing after pop",a)