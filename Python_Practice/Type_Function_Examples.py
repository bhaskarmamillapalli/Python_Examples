'''
this program is to demonstrate the usage of Type function.
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

print("Type function")
print("*************************")
print('Hardware details:',Hardware,"Type:",type(Hardware))
print('Operating system:',Os,"Type:",type(Os))
print("Bit_details :",Bit_details,"Type:",type(Bit_details))
print("Configuration Details:",_Config,"Type:",type(_Config))
print("Version :",version,"Type:",type(version))
print("User",user,"Type:",type(user))
print("*************************")