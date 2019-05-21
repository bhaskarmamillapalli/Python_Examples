'''
this program is to demonstrate the usage of id function.
This function displays the location on the hard disk where the variable is stored.
'''



#variable Declaration

Hardware ="song"
Os='Windows'
Bit_details="""64 bit OS"""
_Config='''Microsoft'''
version =10.1
user =1
print("*************************")
print('Hardware details:',Hardware)
print('Operating system:',Os)
print("Bit_details :",Bit_details)
print("Configuration Details:",_Config)
print("Version :",version)
print("User:",user)
print("*************************")

#use the type function in the print

print("Id  function")
print("*************************")
print('Hardware details:',Hardware,"Id",id(Hardware))
print('Operating system:',Os,"Id:",id(Os))
print("Bit_details :",Bit_details,"id:",id(Bit_details))
print("Configuration Details:",_Config,"id:",id(_Config))
print("Version :",version,"id:",id(version))
print("User",user,"id:",id(user))
print("*************************")