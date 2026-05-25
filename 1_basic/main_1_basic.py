print('cara panggil file  di terminal = python3 main.py')
name='bekka'
age=35
print(f"Halo, nama saya {name}, umur saya {age} tahun")
if age > 30:
  print('senior') 
else:
  print('junior')

print('DAY 2')

numbers = [1,2,3,4,5]
names=['Andi', 'Budi', 'Caca']
print(numbers)
print(names)

print(names[0])
print(names[1])
names.append('Dada')
print(names)

print('===================')
for name in names:
  print(name)

print('== DICTIONARY ==')
user = {
  "name": "Guitherez",
  "age": 35,
  "isActive": True
}
print(user)
print(user['name'])
print(user['age'])

user['age'] = 36
print(user['age'])
user['city'] = 'bandung'
print(user)

for key, value in user.items():
  print(key, value)

users1 = [
  {"name": "Andi", "age": 20},
  {"name": "Budi", "age": 30},
  {"name": "Caca", "age": 25},
]

for user in users1:
  # print(user)
  print(user['name'], user['age'])

numbers1 = [1,2,3,4,5,6,7,8,9,10]
for number in numbers1:
  if(number % 2 == 0): 
    print(number, ' - Genap')
  else: 
    print(number, ' - Ganjil')

user1 = {
  'name': 'becca',
  'age': 1
}

if(user1['age'] < 2):
  print('bayi ')
else:
  print('Anak-anak')

users2 = [
    {"name": "Andi", "age": 20},
    {"name": "Budi", "age": 35},
    {"name": "Caca", "age": 28}
]

for user in users2:
  if(user['age'] > 30):
    print(user['name'],' - Senior')
  else: 
    print(user['name'],' - Junior')

for user in users2:
  if(user['age'] > 25):
    status = "Senior" if user['age'] > 30 else "Junior"
    print(f"{user['name']} - {user['age']} - {status}")

print(' == DAY 3 == ')
def greet():
  print('hello')
greet()

def greet(name):
  print('Hello,', name)

greet('guitherez')

def add(a,b):
  return a + b

result = add(3,4)
print(result)

fruits = ['apple', 'banana', 'orange']
print(fruits[0])
fruits.append('mango')
print(fruits)
for fruit in fruits:
  print(fruit)

user2 = {
  "name": 'Guitherez',
  "age": 35,
  "isLoggedin": True
}
print(user2['name'])
for key, value in user2.items():
  print(key, value)

print('== Mini Project ==')
todos = []
def addTodo(task):
  todos.append(task)
def _showTodos():
  for i, task in enumerate(todos):
    print(i+1, ".", task)

addTodo('wake up')
addTodo('pray')
addTodo('read news')
addTodo('learn AI')
_showTodos()

todos2 = [{
  'id': 0,
  'name': 'dika',
  'task': 'read',
  'isDone': False
}]

kaka = {
  'id': 1,
  'name': 'kaka',
  'task': 'write',
  'isDone': False
}
mama = {
  'id': 2,
  'name': 'mama',
  'task': 'teach',
  'isDone': False
}
adek = {
  'id': 3,
  'name': 'genie',
  'task': 'music',
  'isDone': False
}
kakak = {
  'id': 4,
  'name': 'gayatri',
  'task': 'drink',
  'isDone': False
}
def addTodo2(user):
  todos2.append(user)

def deleteTodo2(id):
  # pop = id sebagai index, tidak cocok untuk delete model object dengan key Id
  for i,user in enumerate(todos2):
    if user['id'] == id:
      print(i)
      todos2.pop(i)
      break

def updateTodo2(id):
  for user in todos2:
    if user['id'] == id:
      user['isDone'] = True
      break

addTodo2(kaka)
addTodo2(mama)
addTodo2(adek)
deleteTodo2(3)
addTodo2(kakak)
updateTodo2(1)
updateTodo2(0)
deleteTodo2(4)

print(todos2)

print('== Refactor Day 3 ==')
# ===========================
# DATA LAYER (Storage)
# ===========================

