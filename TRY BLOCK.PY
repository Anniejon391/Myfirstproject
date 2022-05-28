#TRY BLOCK IN PYTHON
from asyncore import write
from cmath import e
from this import d


try:
    a=10/5  
except Exception as e:
    print(e)
else:
    print(a)

try:
    a=10/2
except Exception as w:
    print(w)
else:
    print(a)
finally:
    print('thank you')

#TYPE OF EXCEPTIONS IN PYTHON
print(dir(locals()['__builtins__']))
print(len(dir(locals()['__builtins__'])))

#NAMEERROR EXCEPTION

try:
    print(c2)
except Exception as c3:
    print('c2 is not  defined')

try:
    print(10/0)
except Exception as e:
    print('denominator cant be zero')

#VALUE ERROR EXCEPTION
try:
    a=int('varma')
except ValueError as e:
    print('please enter number only')

try:
    a=[10,20,30,40]
    print(a[3])
except IndexError as e:
    print('invalid index')

try:
    f=open('test.txt')
except FileNotFoundError:
    print('file not found')
else:
    print(f.read())

#HANDLING MULTIPLE EXCEPTIONS IN PYTHON

try:
    a=10/20
    print(a)
    b=[10,20,30,40]
    print(b[10])
except ZeroDivisionError:
    print('denominator can not be zero')
except IndexError:
    print('index error')