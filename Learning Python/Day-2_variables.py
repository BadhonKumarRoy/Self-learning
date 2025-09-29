# Day 2: 30 Days of Python progrramming
#level 1
first_name = "Asabeneh"
last_name = "Yetayeh"
full_name = first_name + " " + last_name
country = "Finland"
city = "Helsinki"
age = 250
year = 2023
is_married = False
is_true = True
is_light_on = True
first_name, last_name, country, city, age, year, is_married, is_true, is_light_on = "Asabeneh", "Yetayeh", "Finland", "Helsinki", 250, 2023, False, True, True

#Level 2
print(type(first_name))
print(len(full_name))
print(len(first_name) > len(last_name))
num_one = 5
num_two = 4
print("num_one: ", num_one)
print("num_two: ", num_two)
total = num_one + num_two
print("Total: ", total)
diff = num_one - num_two
print("Difference: ", diff)
product = num_one * num_two
print("Product: ", product)
division = num_one / num_two
print("Division: ", division)
remainder = num_one % num_two
print("Remainder: ", remainder)
exp = num_one ** num_two
print("Exponent: ", exp)
floor_division = num_one // num_two
print("Floor Division: ", floor_division)
radius = 30
print("Radius of a circle: ", radius)
area_of_circle = 3.14 * radius**2
Circum_of_circle = 2 * 3.14 * radius
print("Area of circle: ", area_of_circle)
print("Circumference of circle: ", Circum_of_circle)
input_radius = input("Enter radius: ")
area_of_circle = 3.14 * int(input_radius)**2
Circum_of_circle = 2 * 3.14 * int(input_radius)
print("Area of circle: ", area_of_circle)
print("Circumference of circle: ", Circum_of_circle)
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
country = input("Enter your country: ")
age = input("Enter your age: ")
print("Your first name is ", first_name)
print("Your last name is ", last_name)
print("You are from ", country)
print("You are ", age, " years old.")
help('keywords')