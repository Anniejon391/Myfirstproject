from unicodedata import name


def welcome():
    print('welcome hackers')

welcome()
welcome()
welcome()

#NO RETURN TYPE WITHOUT ARGUMENT FUNCTION IN PYTHON
def add():
    a=int(input('Enter the value of a : '))
    b=int(input('Enter the value of b : '))
    c=a+b
    print('total',c)

add()

#NO RETURN TYPE WITH ARGUMENT FUNCTION IN PYTHON

def sub(a,b):
    c=a-b
    print('difference',c)

sub(25,2)

# RETURN TYPE WITHOUT ARGUMENT FUNCTION IN PYTHON
def mul():
    a=int(input('enter the value of a : '))
    b=int(input('Enter the value of b : '))
    c=a*b
    return c

x=mul()
print('mul',x)

#RETURN TYPE WITH ARGUMENT FUNCTION IN PYTHON
def div(a,b):
    c=a/b
    return c

x=div(25,2)
print('division',x)

#ARBITARY ARGUMENTS FUNCTION IN PYTHON (*)

def class_10(*students):
    print(students) #*STAR INDICATIES ARBITARY FUNCTION
    for user in students:
        print(user)

class_10('ram','sam','raja')

def hack(*teacher):     #ARBITARY ARGUMENTS CAN PASS A LOT OF DATA IT CAN USING IN LOOP FUNCTION ALSO
    print(teacher)
    for user3 in teacher:
        print(user3) 
    
hack('ravi varma','adathiya')

#KEYWORD ARGUMENTS FUNCTION IN PYTHON

def message(name,age):
    print(name,'age is ',age)

message('varma',25)

def answer(name,age):
    print(name,'age is',age)

answer(age=25,name='adathi')    #variable name used in keyword function is called keyword argument

#ARBITARY KEYWORD ARGUMENTS IN PYTHON

def biodata(**data):
    print(data)

biodata(name='adathiya',age=25,gender='male')

#DEFAULT PARAMETER FUNCTION IN PYTHON

def user(name,city='salem'):
    print(name,'is from',city)

user('adathi','namakal')
user('sam')

#PASSING LIST AS AN ARGUMENT IN FUNCTION PYTHON

def total(mark):
     return sum(mark)

print('total : ',total([55,75,80,95,47]))

#RECURSIVE FUNCTION

def factorial(x):
    if x==1:
        return 1
    else:
        return(x*factorial(x-1))

print('factorial : ',factorial(5))
#FACTORIAL(5)
#5*factorial=x-1
#5*factorial=5-1
#5*factorial=4
#5*4*3*2*1

def fact(y):
    if y==1:
        return 1
    else:
        return(y*fact(y-1))

print('fact : ',fact(6))