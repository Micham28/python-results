#Michael McAlexander
#function: A True or False flag, for the parameter of 100<=x<=500 and is a mult of 4.
#verifications tests: 104, 516, 221.

#function:B takes a valid sentence and displays the sentence and number of words.


#A

def is_valid(x):
    valid=False
    if x>=100 and x<=500:
        if x%4==0:
            valid=True
    print('the function is: ',valid)
is_valid(104)
is_valid(516)
is_valid(221)

#B
print('')

def num_words(x):
    w_count=0
    c_c=0
    splt_str=x.split()
    w_count=len(splt_str)
    print("your sentence is: ",x)
    print('your number of words: ',w_count)
num_words('Today is a beautiful day!')
num_words('Hello!')
