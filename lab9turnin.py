#Michael McAlexander

#1

def main():
    print('this program shows you the total amount of calories you intake based on grams.')
    cal_f=0
    cal_c=0
    total=0
    user_fat=int(input('enter the amount of fat grams: '))
    user_carb=int(input('enter the amount of carb grams: '))
    cal_f=cal_fat(user_fat)
    cal_c=cal_carbs(user_carb)
    total=(cal_f+cal_c)
    print('the total calories for this calulation is: ',total)
    print('the total fat calories: ',cal_f)
    print('the total carb calories: ',cal_c)
        

def cal_fat(n):
    c_f=n*9
    return c_f
def cal_carbs(n):
    c_c=n*4
    return c_c

main()
