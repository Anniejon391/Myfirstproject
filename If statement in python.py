# IF STATEMENT IN PYTHON
'''
WRITE A PROGRAM TO CHECK THE GIVEN NUMBER IS EVEN NO
'''

m=int(input('Enter the number : '))
if m%2==0:
    print(m,'is even number')
else:
    print(m,'is odd number')

#IF ELSE STATEMENT IN PYTHON
'''
WRITE A PROGRAM TO CHECK VOTE ELIGIBILITY BY ENTER HIS/HER NAME AND AGE
'''
name=input('Enter your name : ')
age=int(input('Enter your age : '))
if age>=18:
    print(name,'your age is',age,'you are eligible for vote')
else:
    print(name,'your age is',age,'you are not eligible for vote')

#ELIF STATEMENT IN PYTHON
'''
1-5 0.5
5-10 1
10-30 5
>30 MEMBERSHIP CANCEL
'''
days=int(input('Enter the days : '))
if(days==0):
    print('Good no fine')
else:
    if(days>=1 and days<=5):
        print('Fine amount : ',days*0.5)
    else:
        if(days>=5 and days<=10):
            print('fine amount is : ',days*1)
        else:
            if(days>=10 and days<=30):
                print('Fine amount is : ',days*5)
            else:
                print('your member ship is cancel')

#NESTED IF STATEMENT IN PYTHON
'''
3 MARKS AS INPUT
TOTAL
AVERAGE
RESULT
IF PASS GRADE
    90-100 A
    80-89  B
    70-79  C
    60-69  D
    ELSE   E
'''
m1=int(input('Enter the mark m1 : '))
m2=int(input('Enter the mark m2 : '))
m3=int(input('Enter the mark m3 : '))
total=m1+m2+m3
average=total/3
print('total : ',total)
print('average : ',average)
if m1>=35 and m2>=35 and m3>=35:
    print('result : pass')
    if average>=90 and average<=100:
        print('grade : A')
    elif average>=80 and average<=89:
        print('grade : B')
    elif average>=70 and average<=79:
        print('grade : c')
    elif average>=60 and average<=69:
        print('grade : D')
    else:
        print('grade : E')
else:
    print('result : fail')
    print('grade : no grade')