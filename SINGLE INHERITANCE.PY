#SINGLE INHERITANCE


from os import name


class nokia:
    company = 'nokia'
    website = 'www.nokia-india.com'

    def contact_details(self):
        print('Address : cherry road,Near new busstand ,salem')

class nokia1200(nokia):
    def __init__(self):
        self.name='nokia1200'
        self.year=2012

    def product_detail(self):
        print('name : ',self.name)
        print('year : ',self.year)
        print('company : ',self.company)
        print('website : ',self.website)

mobile = nokia1200()
mobile.product_detail()
mobile.contact_details()

#MULTIPLE INHERITANCE

class father:
    def fishing(self):
        print('fishining in river')
    def chess(self):
        print('playing chess from father')

class mother:
    def cooking(self):
        print('cooking food')
    def chess(self):
        print('playing chess from mother')

class son(mother,father):
    def ride(self):
        print('riding bicycle')

o=son()
o.chess()
o.ride()
o.cooking()
o.fishing()

#MULTILEVEL INHERITANCE

class grandfather:
    def ownhouse(self):
        print('grand father house')

class father(grandfather):
    def ownbike(self):
        print('fathers bike')

class son(father):
    def ownbook(self):
        print('son have a book')

a22=son()                #ACCESS WITH ONE CLASS
a22.ownbike()
a22.ownhouse()
a22.ownbook()

#FUNCTION OVERRIDING
class Employee:
    def workinghour(self):
        self.hrs=50
    def printhrs(self):
        print('total working hrs : ',self.hrs)

class trainer(Employee):
    def workinghour(self):
        self.hrs=60

    def resethrs(self):
        super().workinghour()

emploees=Employee()
emploees.workinghour()
emploees.printhrs()

trainee=trainer()
trainee.workinghour()
trainee.printhrs()  

#RESET TRAINEE HRS
trainee.resethrs()
trainee.printhrs()

#DIAMOND PROBLEM
class A:
    def display(self):
        print('i am the display of class A')

class B(A):
    def display(self):
        print('i am the display of class B')

class c(A):
    def display(self):
        print('i am the display of class c')

class D(B,c):
    def display(self):
        print('i am the display of class D')

o=D()
o.display()


#DIAMOND PROBLEM
class A:
    def display(self):
        print('i am the display of class A')

class B(A):
    pass
class c(A):
    pass
class D(B,c):
    pass
o=D()
o.display()

#OPERATOR OVERLOADING
'''
a=10
b=20
print(a+b)
a='varma'
b='adathi'
print(a+b)
'''
class addition:
    def __init__(self,a):
        self.a=a

    def __add__(q1,o2):
        return q1.a + q2.a
    def __sub__(q1,o2):
        return q1.a-q2.a

q1=addition(10)
q2=addition(20)

print('total : ',(q1+q2))
print('Difference : ',(q1-q2))
print('total : ',(q1+q2))

#ABSTRACT BASE CLASS 

from abc import ABC, abstractmethod

class reserveBank(ABC):
    @abstractmethod
    def loan(self):pass

    @abstractmethod
    def credit(self):pass

    @abstractmethod
    def debit(self):pass

class HDFC(reserveBank):
    def loan(self):
        print('we can prodide 7.5% intreast loan')

    def credit(self):
        print('HDFC provide credit')

    def debit(self):
        print('HDFC provide debit')

    def card(self):
        print('we provide  credit card')

o=HDFC()
o.credit()
o.debit()
o.loan()
o.card()
