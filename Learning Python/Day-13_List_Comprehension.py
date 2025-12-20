#1
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
list = [num for num in numbers if num <= 0]
print(list)
#2
list_of_lists = [[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
flattened_list = [num for sublist1 in list_of_lists for sublist2 in sublist1 for num in sublist2]
print(flattened_list)
#3
list_of_tuples = [(i, i**0, i**1, i**2, i**3, i**4, i**5) for i in range(0, 11)]
print(list_of_tuples)
#4
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
#output:
#[['FINLAND','FIN', 'HELSINKI'], ['SWEDEN', 'SWE', 'STOCKHOLM'], ['NORWAY', 'NOR', 'OSLO']]
flat_countries = [[country.upper(), country.upper()[:3], city.upper()] for sublist in countries for (country, city) in sublist]
print(flat_countries)
#5
#output:
#[{'country': 'FINLAND', 'city': 'HELSINKI'}, {'country': 'SWEDEN', 'city': 'STOCKHOLM'}, {'country': 'NORWAY', 'city': 'OSLO'}]
country_city_dicts = [{'country': country.upper(), 'city': city.upper()} for sublist in countries for (country, city) in sublist]
print(country_city_dicts)
#6
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
#output
#['Asabeneh Yetaeyeh', 'David Smith', 'Donald Trump', 'Bill Gates']
full_names = [f'{first} {last}' for sublist in names for (first, last) in sublist]
print(full_names)
#7
slope = lambda x1, y1, x2, y2: (y2 - y1) / (x2 - x1) if x2 != x1 else 'undefined'
y_intercept = lambda x, y, m: y - m * x
print(slope(2, 3, 4, 7))
print(y_intercept(2, 3, 2))
#The end