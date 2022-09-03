#Michael McAlexander

#0-36 pocket.
#pocket 0 is green.
#for 1-10 the odd are red and the even numbered areblack.
#11-18 the odd are black and the even are red.
#19-28 the odd are red and the even are black.
#29-36 the odd are black and the even are red.
#if not in this set then write there is no color assigned to that number.

user_pocket=float(input('what whole numbered pocket?: '))

#values.
#my statements used to identify the values i'm looking to define. 
'''
if user_pocket==2 or 4 or 6 or 8 or 10 or 11 or 13 or 15 or 17 or 29 or 31 or 33 or 35 or 20 or 22 or 24 or 26 or 28 :
    print('black')
elif user_pocket==1 or 3 or 5 or 7 or 9 or 19 or 21 or 23 or 25 or 27 or 12 or 14 or 16 or 18 or 30 or 32 or 34 or 36:
    print('red')
elif user_pocket==0:
    print('green')
else:
    print('there is no assigned color for this number')
'''
#exploring other options.
#the way we shoulf do it LOL.

if user_pocket==0:
    print('green')
elif 1<=user_pocket<=10:
    if user_pocket%2==0:
        print('black')
    else:
        print('red')
elif 11<=user_pocket<=18:
    if user_pocket%2==0:
        print('red')
    else:
        print('black')
elif 19<=user_pocket<=28:
    if user_pocket%2==0:
        print('black')
    else:
        print('red')
elif 29<=user_pocket<=36:
    if user_pocket%2==0:
        print('red')
    else:
        print('black')
else:
    print('there is no color assigned to that number.')


#program 1.
#use formula BMI=weight(lb)*703%height(inch)**2.
'''
user_weight=float(input('enter your weight: '))
user_height=float(input('enter your height: '))

BMI=(user_weight*703)/(user_height**2)

if BMI>18.5:
    print('you are underweight')
elif BMI<=25:
    print('you are at an optimal weight')
else:
    print('you are currently over weight')
'''
