import random
import string
LETTERS=string.ascii_letters
NUMS='0123456789'
SPE='-+*%&$!_'
SYMBOLS=LETTERS+NUMS+SPE
len=int(input("Enter Pass.LENGTH:"))
password=NUMS+SPE+SYMBOLS
print(password)