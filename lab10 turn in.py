#Michael McAlexander
def initials(name):
    name_list = name.split()
    for part in name_list:
        print(part[0].upper() + ".", end="")
    return part
#initials("anna marie quinn")

def main():
    print('this program displays initials of the entered name.')
    print('to end this program enter $ in the name space.')
    user_n=input('Enter a name: ')
    while user_n != '$':
        initials(user_n)
        print('')
        user_n=input('enter the next name: ')
main()
