#Day 6 - Tuples
#level 1
#1
tuple1 = tuple()
tuple2 = ()
print(tuple)
print(tuple1)
#2
brothers = ('Ayse', 'Mehmet', 'Ali')
sisters = ('Selma', 'Zeynep', 'Fatma')
print(brothers)
print(sisters)
#3
siblings = brothers + sisters
#4
print(len(siblings))
#5
siblings = list(siblings)
siblings.append('Father')
siblings.append('Mother')
family_members = tuple(siblings)
print(family_members)
#level 2
#1
sibling1, sibling2, sibling3, sibling4, sibling5, sibling6, father, mother = family_members
print(sibling1)
print(sibling2)
print(father)
print(mother)
#2
fruits = ('banana', 'orange', 'mango', 'lemon')
vegetables = ('Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot')
animal_products = ('milk', 'meat', 'butter', 'yogurt')
food_stuff_tp = fruits + vegetables + animal_products
print(food_stuff_tp)
#3
food_stuff_lt = list(food_stuff_tp)
#4
food_stuff_lt = tuple(food_stuff_lt)
print(len(food_stuff_tp))
if len(food_stuff_tp) % 2 == 0:
    print(food_stuff_lt[len(food_stuff_tp) // 2 - 1 : len(food_stuff_tp) // 2 + 1])
else:
    print(food_stuff_lt[len(food_stuff_tp) // 2])
#5
print(food_stuff_tp[:3])
print(food_stuff_tp[-3:])
#6
del food_stuff_tp
#7
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print('Estonia' in nordic_countries)
print('Iceland' in nordic_countries)
#The end