#Day 8 - Dictionaries
#1
dog = {}
print(type(dog))
#2
dog = {
    'name':'Lucky',
    'color':'White',
    'breed':'Labrador Retriever',
    'legs':4,
    'age': 6
}
print(dog)
#3
student = {
    'first_name':'Badhon Kumar',
    'last_name':'Roy',
    'gender':'Male',
    'age':22,
    'marital_status':'Unmarried',
    'skills': ['Python','C++','C','HTML','CSS','JavaScript','Java'],
    'country':'Bangladesh',
    'city':'Dhaka',
    'address': {
        'street':'UngaBunga',
        'Zip_code':1548
    }
}
print(student)
#4
print(len(student))
#5
print(student['skills'])
print(type(student['skills']))
#6
student['skills'][2] = 'React'
student['skills'].append('C')
print(student['skills'])
#7
keys = student.keys()
print(keys)
#8
values = student.values()
print(values)
#9
dct_items = student.items()
print(dct_items,'\n')
#10
student.pop('address')
print(student)
#11
del student
#The end