# PROPERTY DECORATORS GETTER SETTER

class student:
    def __init__(self,total):
        self._total=total

    def average(self):
        return self._total/5.0

    @property
    def total(self):
        return self._total

    @total.setter
    def total(self,t):
        if t<0 or t>500:
            print('invalid total')
        else:
            self._total=t

o=student(450)
print('total : ',o.total)
print('average : ',o.average())
o.total=500
print('total : ',o.total)
print('average : ',o.average())

#PROPERTY METHOD

class student:
    def __init__(self,total):
        self._total=total

    def average(self):
        return self._total/5.0

    def getter(self):                #getter is use for get a value
        return self._total

    def setter(self,t):              #setter is used for set a value
        if t<0 or t>500:
            print('invalid total cannot be change')
        else:
            self._total=t

    total=property(getter,setter)

    o=student(450)
    print('total : ',o.total)
    print('average : ',o.average())
    o.total=350
    print('total : ',o.total)
    print('average : ',o.average())