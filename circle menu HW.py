#Michael McAlexander

#planning.
#circumference=2*math.pi*radius
#area=math.pi*radius**2

#values and variables.
import math
print('this program is designed to calculate circumference and area.')
print('type which answer you would like by using, \'C\' for circumference, \'A\' for area, and for both \'B\'.')
user_res=input('enter here: ')

#decision + response.
if user_res=='C' or user_res=='c':
    radius=int(input('enter the radius of your circle here: '))
    C=2*math.pi*radius
    print('the circumference is: ',format(C,'.2f'))
elif user_res=='A' or user_res=='a':
    radius=int(input('enter the radius of your circle here: '))
    A=math.pi*radius**2
    print('the area is: ',format(A,'.2f'))
elif user_res=='B' or user_res=='b':
    radius=int(input('enter the radius of your circle here: '))
    C=2*math.pi*radius
    A=math.pi*radius**2
    print('the circumference is:',format(C,'.2f'),'and the area is:',format(A,'.2f'))
else:
    print('that is not one of the measurments avalible.')
