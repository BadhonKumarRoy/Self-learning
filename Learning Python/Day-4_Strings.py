#Day 4 - Strings
#1
s1 = 'Thirty'
s2 = 'Days'
s3 = 'Of'
s4 = 'Python'
print(s1 + ' ' + s2 + ' ' + s3 + ' ' + s4)
#2
string2 = 'Coding' + ' ' + 'For' + ' ' + 'All'
print(string2)
#3
company = 'Coding For All'
#4
print(company)
#5
print(len(company))
#6
print(company.upper())
#7
print(company.lower())
#8
print(company.capitalize())
print(company.title())
print(company.swapcase())
#9
print(company[0:6])
#10
print(company.index('Coding'))
print(company.find('Coding'))
#11
print(company.replace('Coding', 'Python'))
#12
string3 = 'Python for Everyone'
print(string3.replace('Everyone', 'All'))
#13
print(company.split())
#14
string4 = 'Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon'
print(string4.split(', '))
#15
print(company[0])
#16
print(len(company) - 1)
#17
print(company[10])
#18
phrase = "Python For Everyone"
words = phrase.split()
Acronym = words[0][0] + words[1][0] + words[2][0]
print(Acronym)
#19
phrase1 = "Coding For All"
words1 = phrase1.split()
Acronym1 = words1[0][0] + words1[1][0] + words1[2][0]
print(Acronym1)
#20
print(company.index('C'))
#21
print(company.index('F'))
#22
print(company.rfind('l'))
#23
sentence = 'You cannot end a sentence with because because because is a conjunction'
print(sentence.index('because'))
#24
print(sentence.rfind('because'))
#25
print(sentence[0:31] + sentence[55:])
#28
substring = 'Coding'
print(company.startswith(substring))
#29
substring1 = 'coding'
print(company.endswith(substring1))
#30
string = '   Coding For All      '
print(string.strip())
#31
variable = '30DaysOfPython'
print(variable.isidentifier())
variable1 = 'thirty_days_of_python'
print(variable1.isidentifier())
#32
list1 = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print('# '.join(list1))
#33
print("I am enjoying this challenge.\nI just wonder what is next.")
#34
print("Name\t\tAge\tCountry\tCity\nAsabeneh\t250\tFinland\tHelsinki")
#35
radius = 10
area = 3.14 * radius ** 2
print("The area of a circle with radius {} is {} meters square.".format(radius, area))
print(f'The area of a circle with radius {radius} is {area} meters square.')
#36
num1 = 8
num2 = 6
print(f'{num1} + {num2} = {num1 + num2}')
print(f'{num1} - {num2} = {num1 - num2}')
print(f'{num1} * {num2} = {num1 * num2}')
print(f'{num1} / {num2} = {num1 / num2}')
print(f'{num1} % {num2} = {num1 % num2}')
print(f'{num1} // {num2} = {num1 // num2}')
print(f'{num1} ** {num2} = {num1 ** num2}')