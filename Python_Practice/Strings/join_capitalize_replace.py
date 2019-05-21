# Example of 3 functions : Join, Capitalize, replace
# +++++++++++++++++++++++++++++++++++++++++++++++++++
'Join Function'
s = '&'
s1 = ('a', 'b', 'c')
print(s.join(s1))  # First print a then '&' then b then '&'

joiner = '-'
title = ("10,20,30")
print(joiner.join(title))
TITLE = ('10', '20')
print(joiner.join(TITLE))
# +++++++++++++++++++++++++++++++++++++++++++++++++++
"CAPITALIZE FUNCTION"
# First character of each word would be converted to upper case.

s = "this is test"
print(s.capitalize())
# +++++++++++++++++++++++++++++++++++++++++++++++++++
'''Replace method'''

s1 = "Python is scripting is and is programming is language"

print(s1.replace("is", "was"))  ## all the occurances of is are replaced by was.
print(s1.replace("is", "was", 2))  ## First 2 occurrances are replaced.
# +++++++++++++++++++++++++++++++++++++++++++++++++++
"""find and rfind method
returns -1 if no match found
returns the index if the match is found.
rfind to search the string from right to left and return the index.
"""
str1 = "python number string example"
str2 = 'rin'
print(str1.find(str2))
str2 = 'l'
print(str1.find(str2))
print(str1.find(str2, 0, 10))  # search for str2 in str1 starting from "0" index to "10th" index.
print(str1.rfind(str2))  # search for str2 in str1 from right to left and return the index when found.
"""# +++++++++++++++++++++++++++++++++++++++++++++++++++
# count function
# calling a a variable and checking substring occurrences..
# count is returned if match found.
"""
str = "welcome to python world"
sub = "l"
# Prints the count of number of times "l" is appearing in the string from left to right.
print("calling a variable and checking the substring count", str.count(sub))

# +++++++++++++++++++++++++++++++++++++++++++++++++++
# strip,lstrip,rstrip
# strip performs both lstrip and rstrtip.
# lstrip :: removes leading white spaces by default on right
# rstrip :: removes trailing white spaces by default on left.

st ="    888888 this is string example..... Wow!!!888888    "
print("Strip example")
print(st.strip())
print(st.lstrip())
print(st.rstrip())
print(st.rstrip('8 '))
print(st.lstrip(' 8'))
print(st.strip(' 8 ,!')) # strip both 8 and !

# +++++++++++++++++++++++++++++++++++++++++++++++++++
"""ljust and rjust
ljust(width,[fill char])

"""

_007= "Python"
print(_007.ljust(8,'*'))
print(_007.rjust(8,'*'))

# +++++++++++++++++++++++++++++++++++++++++++++++++++
#Center : adds the characters both sides of string.

s1 ="test"
print(s1.center(8,'#'))
print(s1.center(9,'*'))
# +++++++++++++++++++++++++++++++++++++++++++++++++++
# isalnum
# isnumberic
# is decimal

s1='ab'
s2='abc10'
s3='10'


# +++++++++++++++++++++++++++++++++++++++++++++++++++