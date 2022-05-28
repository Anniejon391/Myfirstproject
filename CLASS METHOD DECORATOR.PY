from itertools import count


class student:
    count=0           #CLASS METHOD COMMON FOR ALL OBJECT
    def __init__(self,name,age):
        self.name=name
        self.age=age
        student.count+=1
    def printdetails(self):
        print('name : ',self.name,'age : ',self.age)

    @classmethod            #PASSING CLASS ARGUMENT
    def total(cls):         #IT IS CLASS ARGUMENT
        return cls.count
o=student(name='varma',age=21)
o.printdetails()
print('total addmission : ',student.total())

#STATIC METHOD IN PYTHON
 
class stud:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def printDetails(self):
        print('name : ',self.name,'age : ',self.age)
    @staticmethod
    def welcome():
        print('welcome to our instuation')

s1=stud('varma',25)
s1.printDetails()
s1.welcome()
    