# TUPLE IN PYTHON
# IMMUTABLE
# SURROUNDED BY ROUND BRACKETS (1,1,5)

from operator import truth
from re import X


a=(1,2.5,True,'Ram')
print(a)
print(type(a))
print(a[1])
print(a[-1])
print(a[0:2])
b=list(a)
print(b)
b.append('raja')
print(b)
a=tuple(b)
print(a)
print(type(a))

for i in a:
    print(i)

if 'rja' in a:
    print('found')
else:
    print('not found')
print(len(a))

a=(1,)
print(type(a))
del a
a=(1,2,7,4)
b=(5,6,7,8)
c=a+b
print(c)
print(c.count(7))

a=(1,2,7,4)
b=(5,6,7,8)
c=(a,b)
print(c[0])
print(c[1])
print(c[0][1])

x=('varma',)*10
print(x)

a=(1,2,7,4)
print(min(a))
print(max(a))