

user={
    'name':'ram',
    'age':25,
    'is married':'True'
}
print(user)
print(type(user))
print(user['name'])
print(user.get('age'))
print(user.keys())
print(user.values())
print(user.items())

for x in user:
    print(x)
    print(user[x])
    print(x,'',user[x])

for x in user.values():
    print(x)

for x in user.keys():
    print(x)

for x,y in user.items():
    print(x,y)

#CHANGING VALUES
user.update({'gender':'male'})
print(user)

if 'gender' in user:
    print('present')
else:
    print('not')

if 'name' in user:
    print('present')
else:
    print('not')
if 'age' in user:
    print("present")
else:
    print('not')
if 'is married' in user:
    print('present')
else:
    print('not')

user['age']=35
print(user)

user.pop('age')
user.clear()
print(user)

users={
'user1':{
    'name': 'ram',
    'age' : 25,
    'isMarried' : True
    },
'user2':{
    'name': 'ram',
    'age' : 25,
    'isMarried' : False
    }   
}
print(users)