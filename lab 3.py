#michael McAlexander
#program 1 temperatures
print('this program shows your converted temperatures from celsius or fahrenheit')
print('use \'F\' for Fahrenheit and use \'C\' for Celsius.')
choice=input('enter your measurment here: ')
import math
if choice=='F' or choice=='f':
    F=float(input('whats the temperature: '))
    C=(F-32)*(5/9)
    print('converted',C,'C')
elif choice=='C' or choice=='c':
    C=float(input('whats the temperature: '))
    F=9/5*C+32
    print('converted',F,'F')
else:
    print('there is no such temperature!')
'''
#program 2 temperatures range 90-120
print('this program tells you if your number is a value in between 90 and 120')
alert=False
num_1=float(input('enter the value to be checked: '))
if num_1>=120 or num_1<=90:
    alert=True
else:
    alert=False #not needed

if alert==False:
    print('the value is risky.')
else:
    print('this value is ok.')

#3
print('this program tells you if it\'s a leap year')
year_1=float(input('enter the year here: '))
if (year_1%4==0) and(year_1%100!=0) or (year_1%400==0):
    print('this is a leap year')
else:
    print('this is not a leap year')
'''
