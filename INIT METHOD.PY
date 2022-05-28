# INIT METHOD IN PYTHON

from asyncio import proactor_events
from turtle import pen


class user:
    def __init__(self,name):
        print('call when new instance created')
        self.name=name

    def printall(self):
        print('name : ',self.name)

q1=user('varma')
q1.printall()
print(q1.__dict__)
q2=user('adathi')
q2.printall()
print(q2.__dict__)
print(user.__dict__)

#PROPERTY DECORATOR

class user:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        #self.msg=self.name+'is'+str(self.age)+'years old'

    @property
    def msg(self):
        return self.name+'is'+str(self.age)+'years old'

a3=user('varma',25)
print(a3.name)
print(a3.age)
print(a3.msg)
a3.age=43
print(a3.msg)

#PROPERTY DECORATOR GETTER SETTER

class student:
    def __init__(self,total):
        self._total=total

    def average(self):
        return self._total/5.0
    @property
    def total(self):
        return self.total

    @total.setter
    def total(self,t):
        if t<0 or t>500:
            print('invalid tool and cannot change')
        else:
            self._total=t

o=student(450)
print('total : ',o.total)
print('avergae : ',o.average)
o.total=550
print('total',o.total)
print('average : ',o.average)

