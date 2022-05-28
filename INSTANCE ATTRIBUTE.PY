

class user:
    course='java'


o=user()
print(user.__dict__)
print(user.course)         #PRINT CLASS ATTRIBUTE
print(o.course)
print(o.__dict__)
o.course='c++'
print(o.course)
print(o.__dict__)
print(o.course)

o2=user()
print(o2.course)

o2=user.course='c++'
print(user.course)

#CLASS METHODS
class student:
    name='varma'
    age=25

    def printall():
        print('name : ',student.name)
        print('age : ',student.age)

student.printall()
print(student.__dict__)
print(getattr(student,'printall'))
getattr(student,'printall')()

print(student.__dict__['printall'])
student.__dict__['printall']()

#INSTANCE METHOD
class teacher:
    name='varma'          #CLASS ATTRIBUTE
    age=25                #CLASS ATTRIBUTE
    def printall(self,gender):        #SELF IS AN INSTANCE METHOD  AND ALSO ADD PARAMETERS
        print('name : ',teacher.name)
        print('age : ',teacher.age)
        print('gender : ',gender)

a2=teacher()

a2.printall('male')
teacher.printall(a2,'male')