#level 1
#4
from functools import reduce
import data.countries as countries_data
import data.countries_data as countries_Data

countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for country in countries:
    print(country, end=' ')
print()
#5
for name in names:
    print(name, end=' ')
print()
#6
for number in numbers:
    print(number, end=' ')
print()
#level 2
#1
def uppercase(country):
    return country.upper()
uppercased_countries = map(uppercase, countries)
print(list(uppercased_countries))
#2
def square(number):
    return number ** 2
squared_numbers = map(square, numbers)
print(list(squared_numbers))
#3
uppercased_names = map(lambda name: name.upper(), names)
print(list(uppercased_names))
#4
def string_containing_land(country):
    if 'land' in country:
        return True
    else:
        return False
countries_with_land = filter(string_containing_land, countries)
print(list(countries_with_land))
#5
def string_length_six(country):
    if len(country) == 6:
        return True
    else:
        return False
countries_with_length_six = filter(string_length_six, countries)
print(list(countries_with_length_six))
#6
def string_length_greater_than_six(country):
    if len(country) > 6:
        return True
    else:
        return False
countries_with_length_greater_than_six = filter(string_length_greater_than_six, countries)
print(list(countries_with_length_greater_than_six))
#7
def string_starting_with_e(country):
    if country.startswith('E'):
        return True
    else:
        return False
countries_starting_with_e = filter(string_starting_with_e, countries)
print(list(countries_starting_with_e))
#8
def even_number(number):
    if number % 2 == 0:
        return True
    else:
        return False
def add_two_nums(x, y):
    return x + y
chained_operations = reduce(add_two_nums, map(lambda num: add_two_nums(num, num), filter(even_number, numbers)))
print(chained_operations)  # 60
#9
mixed_list = ['Asabeneh', 250, True, 3.14, 'Finland', 2021]
def get_string_lists(lst):
    def is_string(item):
        return isinstance(item, str)
    string_list = filter(is_string, lst)
    return list(string_list)
print(get_string_lists(mixed_list))  # ['Asabeneh', 'Finland']
#10
sum_of_numbers = reduce(lambda x, y: x + y, numbers)
print(sum_of_numbers)  # 55
#11
concatenated_countries = reduce(lambda x, y: x + ', ' + y, countries[:-1]) + ', and ' + countries[-1] + ' are north European countries.'
print(concatenated_countries) #Estonia, Finland, Sweden, Denmark, Norway, and Iceland are north European countries.
#12
def categorize_countries_with_common_pattern(countrys):
    # This function categorizes countries based on common patterns in their names
    # For example, countries ending in 'ia', 'land', or starting with 'E'
    patterns = {
        'ia': [],
        'land': [],
        'island': [],
        'stan': []
    }
    for country in countrys:
        if country.endswith('ia'):
            patterns['ia'].append(country)
        if 'land' in country:
            patterns['land'].append(country)
        if country.startswith('Island'):
            patterns['island'].append(country)
        if country.endswith('stan'):
            patterns['stan'].append(country)

    return patterns
categorize_countries = categorize_countries_with_common_pattern(countries_data.countries)
print(categorize_countries)
#13
def returning_dictionary():
    # This function returns a dictionary, where keys stand for starting letters of countries and values are the number of country names starting with that letter.
    country_dict = {}
    
    total_countries = len(countries_data.countries)
    country_dict['total_countries'] = total_countries

    for country in countries_data.countries:
        first_letter = country[0]
        if first_letter in country_dict:
            country_dict[first_letter] += 1
        else:
            country_dict[first_letter] = 1
    return country_dict

print(returning_dictionary())  # {'total_countries': 195, 'A': 11, 'B': 17, 'C': 16, 'D': 4, 'E': 7, 'F': 3, 'G': 11, 'H': 4, 'I': 9, 'J': 3, 'K': 7, 'L': 9, 'M': 18, 'N': 10, 'O': 1, 'P': 10, 'Q': 1, 'R': 4, 'S': 27, 'T': 11, 'U': 7, 'V': 4, 'Y': 1, 'Z': 1}
#14
def get_first_ten_countries(countrys):
    # This function returns the first ten countries from the list
    return countrys[:10]
print(get_first_ten_countries(countries_data.countries))  # ['Afghanistan', 'Albania', 'Algeria', 'Andorra', 'Angola', 'Antigua and Barbuda', 'Argentina', 'Armenia', 'Australia', 'Austria']
#15
def get_last_ten_countries(countrys):
    # This function returns the last ten countries from the list
    return countrys[-10:]
print(get_last_ten_countries(countries_data.countries))  # ['United States', 'Uruguay', 'Uzbekistan', 'Vanuatu', 'Vatican City', 'Venezuela', 'Vietnam', 'Yemen', 'Zambia', 'Zimbabwe']
#level 3
#1 sort countries by name, by capital, by population
sorted_by_name = sorted(
    countries_Data.countries_data,
    key=lambda country: country["name"]
)
sorted_by_capital = sorted(
    countries_Data.countries_data,
    key=lambda country: country["capital"]
)
sorted_by_population = sorted(
    countries_Data.countries_data,
    key=lambda country: country["population"]
)
sorted_by_population_desc = sorted(
    countries_Data.countries_data,
    key=lambda country: country["population"],
    reverse=True
)
print("____________________________ sorted by name")
print()
print()
print(sorted_by_name)
print("____________________________ sorted by capital")
print()
print()
print(sorted_by_capital)
print("____________________________ sorted by population")
print()
print()
print(sorted_by_population)
print("____________________________ sorted by population desc")
print()
print()
print(sorted_by_population_desc)
print("____________________________")
print()
print()
#2 Sort out the ten most spoken languages by location.
from collections import Counter

language_counter = Counter()

for country in countries_Data.countries_data:
    for language in country["languages"]:
        language_counter[language] += 1

ten_most_spoken_languages = language_counter.most_common(10)
print(ten_most_spoken_languages)
#3 Sort out the ten most populated countries.
ten_most_populated_countries = sorted_by_population_desc[:10]
print(ten_most_populated_countries)
#The End