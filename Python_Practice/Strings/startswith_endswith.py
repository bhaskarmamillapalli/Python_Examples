#!/usr/bin/python
"""
this program is check if a strings start with or ends with in a specific string.
This program returns true or false..
"""
str = "this is python world....lets rock!!!$"

print (str.startswith('this'))
print (str.startswith('python',8))
print (str.startswith('world',1))
print(str.endswith('$'))