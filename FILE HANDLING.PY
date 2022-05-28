
from re import L


file=open('D:\InstallationLog.txt.txt','r')
print(file.read())

try:
    file=open('D:\InstallationLog.txt.txt','r')
    print(file.read())
except FileNotFoundError:
    print('Error : File not found')
else:
    file.close()


try:
    file2=open('varma.txt','r')
    print(file2.readlines())   #it is printed in list format  it is used in data science also
    print(file2.readline(2))   #character wise calling for eg: adathi readline((3)) = ada like that
except FileNotFoundError:                                     #123456 
    print('Error : file not found')
else:
    file2.close()

#LOOP LINE BY LINE IN PYTHON FILE CONCEPT
try:
    file3=open('varma.txt','r')
    for line in file3:
        print(line)

except FileNotFoundError:
    print('Error : file not found')
else:
    file3.close()

#WRITE OR OVERWRITE A FILE IN PYTHON

file4=open('varma','w')
file4.write('most wanted criminal')
file4.close()

file4=open('varma','r')
print(file4.read(1))

