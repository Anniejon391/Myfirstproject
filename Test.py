from pickle import FALSE
from re import S


a=10
b=25
print(a+b)

#CASTING IN PYTHON
a=10
print(a)
print(type(a))
b=float(a)
print(type(b))
c=complex(a)
print(type(c))
print(c)

#INT()
#FLOAT()
#COMPLEX()

a=input('Enter the value of a : ')
b=input('Enter the value of b : ')
c=a+b

print('Total'+c)

#STRING AND STRING FUNCTION
s='varma'
print(s)
print(type(s))
print(s.upper())
print(s.lower())
print(s.capitalize())
print(s.title())
print(s.count('v'))
print(s.endswith('ma'))
print(s.find('r'))
print(s.find('a',2))
print(s.replace('v','s'))

a='JOES22'
print('is upper : ',a.isupper())
print('is lower : ',a.islower())
print(a.lower())
print('is alpha numeric : ',a.isalnum())
print('is alpha : ',a.isalpha())

s='he\nis\ngood'
print(s)
print(s.splitlines())
print(s.splitlines(True))
print(s.splitlines())

a='hackers online learning'
print(a.split(' '))
a='hackers , online , learning'
print(a.split(','))

s='      varma     '
print(len(s))
print(len(s.strip()))
print(len(s.lstrip()))
print(len(s.rstrip()))
s='12-03-2020'
print(s.partition('-'))