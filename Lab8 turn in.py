#Michael McAlexander
#2
def main():
    print('this prgram displays all the squares less than or equal to the integer entered.')
    print('by entering a negative you can end the program')
    print('')
    time=0
    integer=int(input('enter an integer here: '))
    while integer>=0:
        squares_less(integer)
        time+=1
        integer=int(input('enter an integer here: '))
    print('you entered ',time,' non-negative integers.')
    print('thanks for using the program!')

def squares_less(n):
    B=0
    while B**2<=n:
        print(B**2, end=' ')
        B+=1
    print('')
    print('number of squares: ',B)
    print('')
main()

