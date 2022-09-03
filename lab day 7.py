#1 SSN
print('this code take a nin digit number and formats it into social security form')

SSN=input('enter your nine digit SSN here: ')
X=len(SSN)
if X==9:
    print('your SSN in format is',SSN[0:3]+'-'+SSN[3:5]+'-'+SSN[5:9])
else:
    print('incorrect input')


#3 odds and evens

print('this program shows how many digits are even or odd in a given positive number set')
A=(input('enter a positive number here '))
B=len(A)
even=0
odd=0
if int(B)>0:
    for pos in range(B):
        if int(A[pos])%2==0:
            even+=1
        else:
            odd+=1
else:
    print('the entered integer is not posititve')
print('there are', even,'even digits')
print('there are', odd, 'odd digits')
