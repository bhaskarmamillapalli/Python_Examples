#!/usr/tmp

'''
cars =['hyundai','maruti','bmw','toyota']

for car in cars:
    if car =='bmw':
        print(car.upper())
    else:
        print(car.lower())
'''

'''
simple if

age = int(input('enter the age of the person'))

if age <=18:
    print('you are not eligible for voting')
'''

'''
Simple if.
requested_toppings = ['mushrooms', 'extra cheese']

if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")

print("\nFinished making your pizza!")
'''

'''
the following program, will only print adding mushrooms and then come out of the if statement.
the reason is : python would not evaluate any conditions after successful validation of the first condition.
here first validation is mushrooms in extra_toppings.so will not evaluate the extra-cheese

extra_toppings = ['mushrooms','extra-cheese','jalapenos']

if 'mushrooms' in extra_toppings:
    print('adding mushrooms')
elif 'pepperoni' in extra_toppings:
    print('adding pepperoni')
elif 'extra-cheese' in extra_toppings:
    print('adding extra-cheese')
print('Pizza ready with extra toppings')

'''

'''
#if,elif,else:

age = int(input('Enter the age of person ::\n'))
if age <18:
    print('you are not eligible to vote')
    print('please wait:'+str(18-age)+'Years')
elif age ==18:
    print('you can just vote')
    print('Please register')
else:
    print('you are already voting')
'''
