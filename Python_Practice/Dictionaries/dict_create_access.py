guido = {'Name':'Bhaskar','Age':30,'Company':"Oracle"}
print(guido,type(guido),len(guido))
print(dict(enumerate(guido)))
print("Name of the person::",guido['Name'])

print ("guido['Name']: ", guido['Name'])  # Calling Keys

del guido['Name'] # remove entry with key 'Name'
print(guido)
#print("name:",guido['Name'])# this will throw error as the entry with key 'name' is deleted.


guido['Name']='Phani' # update entry to dict.
guido['Module'] ='Fin' # add a new entry to dict.

print('Name of the person ::',guido['Name'])
print('Age is::',guido['Age'])
print("Company is::",guido['Company'])
print("Module:",guido['Module'])
print(guido)

