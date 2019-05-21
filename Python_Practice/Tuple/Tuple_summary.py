'''
A tuple is an immutable sequence of values of any type.
Tuple elements are indexed by sequential integers, starting with zero.
Tuples are constructed by the comma operator,
with or without enclosing parentheses.
An empty tuple must have the enclosing parentheses.
A single item tuple must have a trailing comma.
'''

print(tuple()) # Empty tuple.

tup =1,2,3,4,5
print(tup) # Integer tupe.
print(tuple(tup))

tup1 = '1','2','3'
print(tup1) # Character tupe.
print(tuple(tup1))

tup2 =1, ## single item tuple

print(tup2)

print(tuple(enumerate([1,2,3,4,5]))) # Print the index and the value  available at the index.