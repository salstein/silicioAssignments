#Assignment 1 - Volume of Cylinder,Cone and Cube
''' Volume of Cylinder'''
'''r=float(input('Enter radius of Cylinder'))
h=float(input('Enter height of Cylinder'))
pi=22/7
x=pi*h*(r**2)
print('Volume of the Cylinder is',x)
Volume of Cone
r=float(input('Enter radius of Cone'))
h=float(input('Enter height of Cone'))
pi=22/7
y=(pi*h*(r**2))/3
print('Volume of the Cone is',y)

Volume of Cube
l=float(input('Enter lenght of Cube'))
Z=l**3
print('Volume of the Cube is',y)'''


#Assignment 2 - Simple Calculator
'''a=float(input('Enter first value'))
op=input('Enter an operator')
b=float(input('Enter second value'))
if op=='+':
        print(a+b)
elif op=='-' :
    print(a-b)
elif op=='*' :
    print(a*b)
elif op=='/':
    print(a/b)
else :
    print('Invalid Operator')'''


#Assignment 3 - Student's Result
'''a=float(input('Enter score'))
if 100>=a>=70:
    print('Excellent -A')
elif 69>=a>=60:
    print('Very Good-B')
elif 59>=a>=50:
    print('Good-C')
elif 49>=a>=45:
    print('Fair-D')
elif 44>=a>=40:
    print('Poor-E')
elif 0<=a<40:
    print('Very Poor-F')
else:
    print ('ERROR')'''
#Assignment 4 Odd and Even Number
'''a=int(input('Enter value'))
b=a%2
if b==0:
    print(a,'is an even number')
else:
    print(a,'is an odd number')'''



#Task 1 - Anagram
'''name=input('Enter word or number')
w=name[ : :-1]
if w==name:
    print('Correct')
else:
    print(w,' is Incorrect')'''
#Task 2 - 3 x 3 Matrix
'''a11=float(input('Enter value of a11'))
a12=float(input('Enter value of a12'))
a13=float(input('Enter value of a13'))
a21=float(input('Enter value of a21'))
a22=float(input('Enter value of a22'))
a23=float(input('Enter value of a23'))
a31=float(input('Enter value of a31'))
a32=float(input('Enter value of a32'))
a33=float(input('Enter value of a33'))
U=a11*((a22*a33)-(a23*a32))
V=a12*((a21*a33)-(a23*a31))
W=a13*((a21*a32)-(a22*a31))
A=U-V+W
print('Determinant /A/ is ',A)'''

#Task 3 - Guessing Game
name='snowflake'
print('Hint: falls during Winter')
count=0
while count<3:
        Guess=input('Your Guess...')
        if name==Guess:
             print('You Won!')
             break
        else:
            print(' You have ',(3-(count+1)),' more attempt(s)')
            count+=1
else:
     print('You lost!!!')


