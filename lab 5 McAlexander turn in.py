# Michael McAlexander
# problem 1

print('this is a weight converter')
print('info: 1(lb) is equal to 0.45359237')

user_amt=int(input('how many conversions do you want to make? '))

for t_run in range(user_amt):
    print('conversion #'+str (t_run+1))
    print('***If you want to convert kg to lb, enter 1***')
    print('***If you want to convert lb to kg, enter 1***')
    user_cho=int(input('enter your selection; '))
    if user_cho==1:
        w_kg=float(input('enter weight in kg: '))
        con_1=(w_kg*2.20462262)
        print(w_kg,'kg =',con_1,'lb')
    elif user_cho==2:
        w_lb=float(input('enter weight in lb: '))
        con_2=(w_lb*0.45359237)
        print(w_lb,'lb =',con_2,'kg')
    else:
        print('thats not an option')
