#Level 1
#1
number = list(range(11))
print("For Loop-")
for numbers in number:
    print(numbers, end=" ")
print("\nWhile Loop-")
i = 0
while i < len(number):
    print(i, end=" ")
    i += 1
#2
print("\nFor Loop2-")
for numbers in reversed(number):
    print(numbers, end=" ")
print("\nWhile Loop2-")
i = 10
while i > -1:
    print(i, end=" ")
    i -= 1
#3
print()
for i in range(8):
    for j in range(0,i):
        print("#",end="")
    print()
print()
#4
for i in range(8):
    for j in range(8):
        print("#", end=" ")
    print()
#5
print()
for i in range(11):
    print(f"{i} x {i} = {i*i}")
#6
languages = ['Python','Numpy','Pandas','Django','Flask']
for language in languages:
    print(language, end=" ")
print()
#7
print("Even Numbers:")
for number in range(101):
    if number %2 == 0:
        print(number, end=" ")
print()
#8
print("Odd Numbers:")
for number in range(101):
    if number %2 == 1:
        print(number, end=" ")
print()
#Level2
#1
sum = 0
for number in range(101):
    sum += number
print(f'The sum of all numbers is {sum}.')
#2
sum_even = 0
sum_odd = 0
for number in range(101):
    if number % 2 == 0:
        sum_even += number
    else:
        sum_odd += number
print(f'The sum of all evens is {sum_even}. And the sum of all odds is {sum_odd}.')
#Level3
#1
from data.countries import countries  # import the list of countries

land_countries = []  # empty list to store matches

for country in countries:
    if 'land' in country.lower():  # check if 'land' exists in the name (case-insensitive)
        land_countries.append(country)

print(land_countries)
#2
fruits = ['banana','orange','mango','lemon']
for fruit in reversed(fruits):
    print(fruit, end=" ")
#3
#i
print()
from data.countries_data import countries_data
'''lst = [{
    'name':'ldfk',
    'languages': ["Pashto","Uzbek","Turkmen"]
},
{
    'name':'lkdsfjdkl',
    'languages': ["Pashto","Uzbek","Turkmen"]
}]'''
total_languages = set()
for country in countries_data:
    for language in country['languages']:
        total_languages.add(language)
print(len(total_languages))