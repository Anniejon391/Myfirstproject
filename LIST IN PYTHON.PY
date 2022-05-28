# LIST IN PYTHON
'''
SEQUENCE TYPE
MUTABLE

a[5]
a={1,2,3,4,5}
a[0]
'''
from re import A
from telnetlib import PRAGMA_HEARTBEAT


a=[1,2,3,4,5]
print(a)
print(type(a))
a[0]=100
print(a)
print(a[1])
print(a[-1])
print(a[0:3])
print(a[2:])
print(a[:3])

print('-------------------------------------------------')
a=[1,True,'Ram',2.5,[1,2,3,4,]]
print(a)
print(type(a))
print(type(a[0]))
print(a[0],'type is',type(a[0]))
print(a[1],'type is',type(a[1]))
print(a[2],'type is',type(a[2]))
print(a[3],'type is',type(a[3]))
print(a[4],'type is',type(a[4]))
print(a[4][1])
print('--------------------------------------------')
a=[10,25,35,45]
a.clear()
print(a) 

a=[10,25,35,45]
b=a.copy()
print(b)
a=[10,25,35,45,25,4,25]
print(a.count(25))
print(a.index(25))
print(len(a))
print(max(a))
print(min(a))
print(a)
a.pop(0)  #REMOVE ELEMENT USING INDEX
print(a)
a=[10,25,35,45,25,4,25]
a.remove(45)     # REMOVE VALUES
print(a)

names=['Ram']
print(names)
names.append('sam')
names.append('ravi')
names.append('kumar')
print(names) 
names55=['sara','anitha']
names.extend(names55)
names.insert(0,'surya')
print(names)

print(list(range(6)))
print(list('varma'))
a=[10,50,100,25,85]
print(a)
a.sort()
print(a)
a.sort(reverse=True)
print(a)
a=['orange','apple','zebra']
a.sort()
print(a)
a.sort(reverse=True)
print(a)
a.sort(key=len)
print(a)