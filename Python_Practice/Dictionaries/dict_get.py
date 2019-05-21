student = {'Name':'abc','Age':6,'Class':'2nd'}
print('Print Age is :',student.get('Age'))
print('Print Age is:',student['Age'])

print('Name %s:'%student.get('Name'))
print('Age of %s:is'%student.get('Name'),student['Age'])
print('Age of {} is {}'.format(student['Name'],student['Age']))

print ("Value : %s" %  student.get('Education', "Python")) # education is key and python is value.
print(type(student))

dict_1 = {'Name':'minnu','Age':7}
stri = str(dict_1) # convert dict to string.
print ("Equivalent String : %s" % str(dict_1))  # str() is function
print("string value %s"%stri)

#copy a dictonary value to another variable.
dict_copy = student.copy()
print("value in dict_copy variable",dict_copy)
