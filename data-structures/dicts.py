#students = {}

students = {'name': 'Niles', 'age': 45, 'interests': ['psychology', 'family']}

print(students)
print(students.get('name'))

#returns None where key does not exist
print(students.get('phone'))

#can specify which error to return when key does not exist
print(students.get('phone', 'Not found'))

#add new key, value pair
students['phone'] = '777-7777'
print(students.get('phone'))

#make multiple updates
students.update({'name': 'Frasier', 'age': 50})

#del key, val pair
del students['age']
print(students)

#delate and return the value
interests = students.pop('interests')
print(interests)
print(students)

#see all keys
print(students.keys())

#see all values
print(students.values())

#see all key,val pairs
print(students.items())

#loop through keys
for key in students:
    print(key)

#loop through key,val pairs
for key,val in students.items():
    print(key, val)    



