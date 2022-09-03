#Michael McAlexander

#2 sum of squares

print('this program shows the user the sum of the squares that they enter')  
n=int(input('how mant squares do you want?: '))
total=0
for value in range(1,n+1):
        total+=value**2
print('1^2+2^2+3^2+...',n,'=',total)
