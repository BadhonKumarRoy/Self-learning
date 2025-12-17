#Level1
#1
def add_two_numbers(num1, num2):
    sum = num1 + num2
    return sum
print(add_two_numbers(1,2))
#2
def area_of_circle(r):
    area = 3.1416 * pow(r,2)
    return area
print(area_of_circle(3))
#3
def add_all_nums(*args):
    sum = 0
    for i in args:
        if type(i) == int or type(i) == float:
            sum += i
        elif type(i) != int or type(i) != float:
            print(f'{i} is not a number.')
    print(sum)
add_all_nums(1,2,4,'s',5.2)
#4
def convert_celsius_to_fahrenheit(c):
    f = (c*(9/5)) + 32
    print(f'{c}°C = {f}°F')
convert_celsius_to_fahrenheit(100)
#5
def check_season(month):
    if month == 'September' or month == 'October' or month == 'November':
        print(f'The season is: Autumn.')
    elif month == 'December' or month == 'January' or month == 'February':
        print(f'The season is: Winter.')
    elif month == 'March' or month == 'April' or month == 'May':
        print(f'The season is: Spring.')
    elif month == 'June' or month == 'July' or month == 'August':
        print(f'The season is: Summer.')
    else:
        print("Invalid.")
check_season('August')
#6
def calculate_slope(x,y,b):
    m = (y-b)/x
    return m
x = 2
y = 3
b = 1
print(f'The slope of equation {y} = m{x} + {b} is: {calculate_slope(x,y,b)}.')
#7
def solve_quadratic_eqn(a,b,c):
    d = (b**2) - (4*a*c)
    sol1 = (-b + d**0.5) / (2*a)
    sol2 = (-b - d**0.5) / (2*a)
    return sol1, sol2

print(solve_quadratic_eqn(1,-3,2))
#8
list_of_args = [1,2,3,4,5]
def print_list(args):
    for i in args:
        print(i, end=" ")
print_list(list_of_args)
print()
#9
def reverse_list(args):
    reversed_list = []
    for i in reversed(args):
        reversed_list.append(i)
    return reversed_list
print(reverse_list([1,2,3,4,5]))
print(reverse_list(["A", "B", "C"]))
#10
def capitalize_list_items(args):
    capitalized_list = []
    for i in args:
        capitalized_list.append(i.capitalize())
    return capitalized_list
print(capitalize_list_items(['apple', 'banana', 'orange']))
#11
food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
numbers = [2, 3, 7, 9]
def add_item(lst, item):
    lst.append(item)
    return lst
print(add_item(food_staff, 'Meat'))     # ['Potato', 'Tomato', 'Mango', 'Milk','Meat']
print(add_item(numbers, 5))     # [2, 3, 7, 9, 5]
#12
def remove_item(lst, item):
    lst.remove(item)
    return lst
print(remove_item(food_staff, 'Mango'))  # ['Potato', 'Tomato', 'Milk'];
print(remove_item(numbers, 3))  # [2, 7, 9]
#13
def sum_of_numbers(n):
    sum = 0
    for i in range(n+1):
        sum += i
    return sum
print(sum_of_numbers(5))  # 15
print(sum_of_numbers(10)) # 55
print(sum_of_numbers(100)) # 5050
#14
def sum_of_odds(n):
    sum = 0
    for i in range(n+1):
        if i % 2 != 0:
            sum += i
    return sum
print(sum_of_odds(5))  # 9
print(sum_of_odds(10)) # 25
print(sum_of_odds(100)) # 2500
#15
def sum_of_evens(n):
    sum = 0
    for i in range(n+1):
        if i % 2 == 0:
            sum += i
    return sum
print(sum_of_evens(5))  # 6
print(sum_of_evens(10)) # 30
print(sum_of_evens(100)) # 2550
#level2
#1
def evens_and_odds(n):
    even_count = 0
    odd_count = 0
    for i in range(n+1):
        if i % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    print(f'The number of evens are {even_count}.')
    print(f'The number of odds are {odd_count}.')
evens_and_odds(100)
    # The number of odds are 50.
    # The number of evens are 51.
#2
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)
print(factorial(5))  # 120
print(factorial(10)) # 3628800
print(factorial(0))  # 1
#3
def is_empty(param):
    if param:
        return False
    else:
        return True
print(is_empty([]))        # True
print(is_empty([1, 2, 3])) # False
print(is_empty(""))        # True
print(is_empty("Hello"))   # False
#4
def calculate_mean(nums):
    total = sum(nums)
    mean = total / len(nums)
    return mean
print(calculate_mean([1, 2, 3, 4, 5]))  # 3.0
print(calculate_mean([10, 20, 30]))      # 20.0
print(calculate_mean([-5, 0, 5]))        # 0.0

def calculate_median(nums):
    sorted_nums = sorted(nums)
    n = len(sorted_nums)
    mid = n // 2
    if n % 2 == 0:
        median = (sorted_nums[mid - 1] + sorted_nums[mid]) / 2
    else:
        median = sorted_nums[mid]
    return median
print(calculate_median([1, 3, 3, 6, 7, 8, 9]))  # 6
print(calculate_median([1, 2, 3, 4, 5, 6, 8, 9])) # 4.5

def calculate_mode(nums):
    frequency = {}
    for num in nums:
        frequency[num] = frequency.get(num, 0) + 1
    max_freq = max(frequency.values())
    modes = [num for num, freq in frequency.items() if freq == max_freq]
    return modes
print(calculate_mode([1, 2, 2, 3, 4]))        # [2]
print(calculate_mode([4, 4, 1, 2, 2, 3, 3]))  # [4, 2, 3]

def calculate_range(nums):
    range_value = max(nums) - min(nums)
    return range_value
print(calculate_range([1, 2, 3, 4, 5]))  # 4
print(calculate_range([-10, 0, 10]))     # 20

def calculate_variance(nums): #Unclear about this one
    mean = calculate_mean(nums)
    variance = sum((x - mean) ** 2 for x in nums) / len(nums)
    return variance
print(calculate_variance([1, 2, 3, 4, 5]))  # 2.0
print(calculate_variance([10, 20, 30]))      # 66.66666666666667

def calculate_std_deviation(nums): #Unclear about this one
    variance = calculate_variance(nums)
    std_deviation = variance ** 0.5
    return std_deviation
print(calculate_std_deviation([1, 2, 3, 4, 5]))  # 1.4142135623730951
print(calculate_std_deviation([10, 20, 30]))      # 8.16496580927726

#level3
#1
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
print(is_prime(11))  # True
print(is_prime(15))  # False
print(is_prime(2))   # True
print(is_prime(1))   # False
#2
def check_unique(lst):
    return len(lst) == len(set(lst))
print(check_unique([1, 2, 3, 4, 5]))      # True
print(check_unique([1, 2, 2, 3, 4]))      # False
print(check_unique(['a', 'b', 'c']))      # True
print(check_unique(['a', 'b', 'a']))      # False
#3
def check_data_type_in_list(lst):
    for item in lst:
        if not isinstance(item, type(lst[0])):
            return False
    return True
print(check_data_type_in_list([1, 2, 3, 4]))        # True
print(check_data_type_in_list([1, 2, '3', 4]))       # False
print(check_data_type_in_list(['a', 'b', 'c']))      # True
print(check_data_type_in_list(['a', 'b', 3]))        # False
#4
def check_valid_variable_name(name):
    import keyword
    if not name.isidentifier() or keyword.iskeyword(name):
        return False
    return True
print(check_valid_variable_name('variable1'))  # True
print(check_valid_variable_name('1variable'))  # False
print(check_valid_variable_name('for'))        # False
print(check_valid_variable_name('my_var'))     # True
#5
import ThirtyDaysOfPython.data.countries_data as cd

def most_spoken_languages(n=10):
    """Return n most spoken languages in descending order"""
    count = {}
    
    for country in cd.countries_data:
        for lang in country['languages']:
            count[lang] = count.get(lang, 0) + 1

    sorted_langs = sorted(count.items(), key=lambda x: x[1], reverse=True)
    return sorted_langs[:n]

top_10 = most_spoken_languages(10)
for lang, num in top_10:
    print(f"{lang}: {num} countries")

def most_populated_countries(n=10):
    """Return n most populated countries in descending order"""
    sorted_countries = sorted(cd.countries_data, key=lambda x: x['population'], reverse=True)
    return [(country['name'], country['population']) for country in sorted_countries[:n]]
top_10_populated = most_populated_countries(10)
for country, population in top_10_populated:
    print(f"{country}: {population}")
#The end