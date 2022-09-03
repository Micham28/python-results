#Michael McAlexander


#main
def main():
    print('this program allows you to practice division and division remainders.')
    print('')
    print('if you would like to practice integer division enter "1".')
    print('if you would like to practice remainders after division enter "2".')
    print('')
    import random
    total=0
    more='yes'
    u_choice=input('Enter your practice selection: ')
    if u_choice=='1':
        while more=='yes':
            rand_1=random.randint(-50,50)
            rand_2=random.randint(1,10)
            u_correct=int_division(rand_1,rand_2)
            total+=1
            more=input('Do you want more practice?(yes/no) ')
    elif u_choice=='2':
        while more=='yes':
            rand_1=random.randint(-50,50)
            rand_2=random.randint(1,10)
            u_correct=remainder(rand_1,rand_2)
            total+=1
            more=input('Do you want more practice?(yes/no) ')
    else:
        print('Thats not an option buddy.')
    print('you completed ',total,' exercises.')
    print('you answered ',u_correct,' correctly.')

#opt_1 integer division
def int_division(x,n):
    correct=0
    quo=int(x//n)
    print(x,'//',n,'=')
    u_answer=int(input('Enter your answer: '))
    if u_answer==quo:
        print('You are correct!')
        correct+=1
    else:
        print('That is not the correct answer, the correct answer is: ',quo)
    return correct

#opt_2 integer remainder
def remainder(x,n):
    correct=0
    quo=int(x%n)
    print(x,'%',n,'=')
    u_answer=int(input('Enter your answer: '))
    if u_answer==quo:
        print('You are correct!')
        correct+=1
    else:
        print('That is not the correct answer, the correct answer is: ',quo)
    return correct
main()
