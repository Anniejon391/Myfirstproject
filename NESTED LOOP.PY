# NESTED FOR LOOP
'''
*
**
***
****
*****

*****
****
***
**
*
'''
'''
ABCDE
ABCDE
ABCDE
ABCDE
ABCDE
'''
# A-Z =>65-90
# a-z =>97-122
for i in range(5):
    for j in range(i):
        print('*',end='')
    print('')

print('--------------------------------------------')

for i in range(5,0,-1):
    for j in range(i):
        print('*',end='')
    print('')

for i in range(65,70,1):
    print(chr(i))

for a in range(97,122,1):
    print(chr(a))

for b in range(97,102,1):
    print(chr(b))

for h in range(5,10,1):
    for k in range(h):
        print('*',end='')
    print('')

for a in range(5,10,2):
    for h in range(a):
        print('*',end='')
    print('')

for i in range(65,70,1):
    for j in range(64,70,1):
        print(chr(j),end='')
    print('')
