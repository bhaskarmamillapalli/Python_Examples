t1 = ("python","Linux",1999,2000)
t2 =(1,2,3,4,5)
t3 ="a","b","c""d"
t4 ='a','b','c','d'

print(t1,type(t1),len(t1),id(t1))
print(t2,type(t2),len(t2),id(t2))
print(t3,type(t3),len(t3),id(t3))
print(t4,type(t4),len(t4),id(t4))

# accessing the tuple value by index.
print(t1[1])
print(tuple(enumerate(t1)))