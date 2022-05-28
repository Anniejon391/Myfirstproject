#STRING MANIPULATION IN PYTHON
from re import A, S
from telnetlib import PRAGMA_HEARTBEAT


s='sample'
print(s)
print(s[0:2])
print(s[:5])
print(s[1:])
print(s[-1])
print(s[-2:-1])
print(s[:-1])
print(s[::-1])

#ARITHMETIC OPERATORS
'''
+ ADDITION
- SUBTRACTION
* MULTIPLICATION
/ DIVISION
% MODULUS
** EXPONENTIATION
// FLOOR DIVISION
'''
a=123
b=10
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)  #FOR REMOVE A DECIMAL POINT FUNCTION
print(a%b)   #FOR GET A REMAINDER
print(2**3)  #ITS A EXPONENTIAL FUNCTION

#ASSIGNMENT OPERATOR
'''
=  ASSIGNMENT
+= ADDITION
-= SUBTRACTION
*= MULTIPLICATION
/= DIVISION
%= MODULUS
**= EXPONENTIAL
//= FLOOR DIVISION
'''
a=125
print(a)
a+=5      #a=a+5
print(a)
a-=10     #a=a-10
print(a)
a*=10
print(a)
a/=10
print(a)  #a=a/=10
a%=10
print(a)
a**=10
print(a)

#COMPARISION OPERATOR OR RELATIONAL OPERATOR
'''
== EQUAL
!= NOT EQUAL
>  GREATER THAN 
<  LESS THAN
>= GREATER THAN OR EQUAL
<= LESS THAN OR EQUAL TO     
'''
a=10
b=20
print(a==b)
print(a!=b)
print(a>b)
print(a<b)
print(a>=b)
print(a<=b)

#LOGICAL OPERATIONS IN PYTHON
'''
AND
OR
NOT
10-20
'''
a=25
print(a>=10 and a<=20)  #IF TWO CONDITION IS TRUE THE OUTPUT ALSO TRUE
print(a>=10 or a<=20)   #if ONE CONDITION IS TRUE THE  OUTPUT ALSO TRUE
print(not(a>=10 and a<=20)) #IT IS OPPOSITE TO AND OPERATOR

# BITWISE OPERATORS
'''
&  AND
|  OR
^  XOR
~  NOT
<< ZERO FILL LEFT SHIFT
>> SIGNED RIGHT SHIFT 
'''
a=25
b=45
print(a&b)
print(a|b)
print(a^b)
print(~a)
print(a<<2)
print(a>>2)


