list1 = ['a','b',1,2,'c']
list2 = [3,4,5,6,7,8,9]

print(list1)
print(list2)

list1.extend('d')
print(type(list1),id(list1),list1)
list2.extend([[1,2]])
print(list2)
list2.extend(list1)
print(list2)