t1,t2 =('linux','abc','def','ghi'),(456,789,234)
#Print min and max value in tuple.

print("Min value " ,min(t1))
print("Max value",max(t1))

print("min value",min(t2))
print("max value",max(t2))

alist = list(t1) # Convert tuple to list.
print(type(alist),alist)

atup = tuple(alist) # convert the list back to tuple
print(type(atup),atup)
