from unicodedata import name


class car():
    pass

a=10
b=20+1j
print(type(a))
print(type(car))
swift=car()
print(isinstance(swift,car))
print(isinstance(a,int))
print(isinstance(b,complex))
print(type(swift))

#CLASS ATTRIBUTE IN PYTHON
class student():
    name='ram'
    age=25

#GETATTR METHOD
print(getattr(student,'name'))
print(getattr(student,'age'))
print(getattr(student,'gender','no such attribute found'))

# DOT NOTATION
print(student.name)
print(student.age)

#SETATTR
setattr(student,'name','varma')
print(student.name)

setattr(student,'gender','male')          #IT ALSO CREATE A NEW ATTRIBUTE
print(student.gender)

student.city='singapore'
print(student.city)

print(student.__dict__)
delattr(student,'city')
print(student.__dict__)
del student.gender
print(student.__dict__)