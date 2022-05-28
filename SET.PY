from tkinter.font import names
from unicodedata import name


names={'ram','sam','ravi'}
print(names)
print(type(names))

#ACCESS VALUE USING FOR LOOP
for name in names:
    print(name)
    
#ADDING NEW ELEMENT 
names.add('sara')
print(names)

#UPDATE ANOTHER SET OF DATA
a={'kumar','sundar','suresh'}
names.update(a)
print(names)
names.remove('kumar')
print(names)
names.discard('kumar')
print(names)
names.pop()
print(names)
names.clear()
print(names)
del names

name5={'ram','ram','sam','ravi','kumar','sundar','suresh'}
print(name5)

a={1,2,3,4}
b={'a','b','c','d'}
c=a.union(b)
print(c)
a.update(b)
print(a)

a={1,2,3,4,5}
b={5,6,7,8,9}
c=a.intersection(b)
print(c)
a.intersection_update(b)
print(a)


a={1,2,3,4,5}
b={5,6,7,8,9}
c=a.symmetric_difference(b)
print(c)
a.symmetric_difference_update(b)
print(a)


a={5,6,7}
b={5,6,7}
c=a.isdisjoint(b)  #IF BOTH THE VALUES ARE DISJOINT IT WILL TRUE
print(c)

c=a.issubset(b)   #IF SOME VALUES ARE EQUAL IN BOTH VALUES IT WILL TRUE
print(c)    

c=a.issubset(b)  #IF BOTH THE VALUES ARE EQUAL IT WILL TRUE
print(c)      
