#WHILE LOOP
'''
1.WHILE LOOP
2.FOR LOOP
'''
from re import I
from socket import if_indextoname


i=1
while i<=10:
    print(i)
    i+=1

#EVEN NO
print('even no')
n=20
i=2
while i<=20:
    print(i)
    i+=2

#CONTINUE STATEMENT
i=1
while i<=20:
    if i%2==0:
        i=i+1
        continue
    print(i)
    i+=1

#BREAK STATEMENT
i=1
while i<=20:
    if i==7:
        break
    print(i)
    i+=1

#RANGE IN PYTHON
'''
1-5  =>1,2,3,4,5
0-5  =>2,4
range(5) =>0,1,2,3,4
range(2,5)
'''
print(list(range(5)))
print(list(range(2,5)))
print(list(range(0,21,2)))
print(list(range(1,20,2)))

#FOR LOOP IN PYTHON
for i in range(5):
    print(i)
for j in range(1,21,2):
    print(j)    
     
for a in range(0,21,2):
    print(a)

for d in range(5):
    a=int(input('Enter the no : '))
    b=int(input('Enter  the no : '))
    print(a+b)

#NESTED FOR LOOP
'''
*
**
***
****
*****
'''
for i in range(5):
    for j in range(i):
        print('*',end='')
    print('')