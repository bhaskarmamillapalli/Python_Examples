'''
List is a mutable data type.
list with zero elemets is empty list.
list elements are indexed by integers starting with 0

lists are constructed with square brackets seprated by comma
[]

POP() -- remove the item by position (index)
remove() -- remove the first item of the list by a value.. if no such value found,returns error.
count (x) -- returns the number of times,x appears in the list.

'''
a= [1,2,9,6,8]
a1=[(1,2),'abc',"def",3,['a','b','c']]
c= 'abc'
print(a)
print (a1)
print(list()) # This prints a empty list.
print(list(a))
print(list(c)) # This prints the output in list format.(convert a string to list)

print (list([1, 2, 3, 4, 5]))
print (list(enumerate(['a', 'b', 'c', 'd'])))
print(list(enumerate(c))) # Prints the list values along with the indexes.

"""
apend : used to add a item at the end of list.
extend : used to add multiple items at the end of list.

"""
print("Printing the list functions")
numbers =[1,2,4,5]
number1 =[1,2,4,5]

numbers.append([6,7]) # add an item to end of list.
print('append',numbers)
number1.append(6)
print("append",number1)

print('Add multiple items at end of list.')
numbers.extend([[7,8,9]]) # add multiple item at the end of list..if you want to get the values in "[]" then
print(numbers)
number1.extend([7,8,9])
print(number1)
"""
Insert :: inserts a value in list based on the index.the value is inserted before the specified index.
variable.insert(i, x)  i is index and x is the value.
"""
numbers.insert(2,3) # Before 2nd index, insert a value 3
print("Insert function:",numbers)
number1.insert(7,10)
print(number1)

'''reverse a list'''

numbers.reverse()
print(numbers)

numbers.remove(2)
print(numbers)
