#Day 9 - Conditionals
#Level 1
#1
age = int(input("Enter your age: "))
if age >= 18:
    print("You are old enough to learn to drive.")
else:
    print("You need", 18-age, "more years to learn to drive.")
#2
my_age = 22
his_age = int(input("Enter your age: "))
if his_age > my_age:
    if (his_age - my_age) == 1:
        print("You are 1 year older than me.")
    else:
        print("Yor are", his_age-my_age, "years older than me.")
elif his_age < my_age:
    if (my_age - his_age) == 1:
        print("I'm 1 year older than you.")
    else:
        print("I'm", my_age-his_age, "years older than you.")
else:
    print("We are of the same age.")
#3
a = int(input("Enter number one: "))
b = int(input("Enter number two: "))
if a>b:
    print(a,"is greater than",b)
elif a<b:
    print(a,"is smaller than",b)
else:
    print(a,"is equal to",b)
#Level 2
#1
score = int(input("Enter your score: "))
if score > 79 and score < 101:
    print("A")
elif score > 69 and score < 80:
    print("B")
elif score > 59 and score < 70:
    print("C")
elif score > 49 and score < 60:
    print("D")
elif score > -1 and score < 50:
    print("F")
else:
    print("Invalid Score")
#2
month = str(input("Enter the month: "))
Autumn = ['September', 'October', 'November']
Winter = ['December', 'January', 'February']
Spring = ['March', 'April', 'May']
Summer = ['June', 'July', 'August']
if month in Autumn:
    print("The season is Autumn.")
elif month in Winter:
    print("The season is Winter.")
elif month in Spring:
    print("The season is Spring.")
elif month in Summer:
    print("The season is Summer.")
else:
    print("Invalid input.")
#3
fruits = ['banana', 'orange', 'mango', 'lemon']
Fruit = str(input("Enter a fruit: "))
if Fruit not in fruits:
    fruits.append(Fruit)
    print(fruits)
else:
    print(Fruit,"is in the list.")
#Level 3
#1
person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}
if 'skills' in person:
    length = len(person['skills'])
    print("The middle skill in the skills list is:",person['skills'][length//2])
else:
    print("The skills key dosen't exist is person dct.")
#...
if 'skills' in person:
    if 'python' in person['skills']:
        print("He is a python developer.")
    else:
        print("He is not a python developer.")
else:
    print("The person has no skills.")
#..
if 'React' and 'Node' and 'MongoDB' in person['skills']:
    print('He is a fullstack developer.')
elif 'JavaScript' and 'React' in person['skills']:
    print("He is a front end developer.")
elif 'Node' and 'Python' and 'MongoDB' in person['skills']:
    print("He is a backend developer.")
else:
    print('unknown title.')
#..
if person['is_marred'] and person['country'] == 'Finland':
    print(f"{person['first_name']} {person['last_name']} lives in {person['country']}. He is married.")
else:
    print(f"{person['first_name']} {person['last_name']} lives in {person['country']}. He is not married.")
#The end