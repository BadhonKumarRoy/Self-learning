#Day 3 - Operators
#1
age = 22
#2
height = 1.75
#3
complex_number = 3 + 4j
#4
base = float(input("Enter the base of a triangle: "))
height = float(input("Enter the height of the triangle: "))
area = 0.5 * base * height
print("The area of the triangle is", area)
#5
side_a = float(input("Enter side a: "))
side_b = float(input("Enter side b: "))
side_c = float(input("Enter side c: "))
perimeter = side_a + side_b + side_c
print("The perimeter of the triangle is", perimeter)
#6
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))
area = length * width
print("The area of the rectangle is", area)
perimeter = 2 * (length + width)
print("The perimeter of the rectangle is", perimeter)
#7
radius = float(input("Enter the radius of the circle: "))
pi = 3.14
area = pi * radius**2
print("The area of the circle is", area)
circumference = 2 * pi * radius
print("The circumference of the circle is", circumference)
#8
# Slope intercept form of a linear equation is y = mx + b
# For the equation 2x - 2y = 0, m = 2 and b = -2
# Therefore, the equation in slope intercept form is
# y = 2x - 2
y = 0
x = int((y + 2) / 2)
print("The x-intercept is (", x, ",", y,")")
x = 0
y = 2 * x - 2
print("The y-intercept is (", x, ",", y,")")
m1 = 2
print("The slope (m) is", m1)
#9
x1, y1 = 2, 2
x2, y2 = 6, 10
m2 = (y2 - y1) / (x2 - x1)
print("The slope (m) is", m2)
distance = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
print("The distance between the points is", distance)
#10
compare_slopes = m1 == m2
print("Are the slopes equal?", compare_slopes)
#11
for x in range(5):
    y = x**2 + 6*x + 9
    if y == 0:
        print("The value of y is 0 for x =", x)
    else:
        print("The value of y is not 0 for x = ", x)
#12
print(len('python') > len('dragon'))
#13
print('on in python and dragon', 'on' in 'python' and 'on' in 'dragon')
#14
print('jargon in I hope this course is not full of jargon', 'jargon' in 'I hope this course is not full of jargon')
#15
print('on not in python and dragon', 'on' not in 'python' and 'on' not in 'dragon')
#16
length = len('python')
length = float(length)
print("The length of 'python' is", length)
length = str(length)
print("The length of 'python' as a string is", length)
#17
for i in range(10):
    if i % 2 == 0:
        print(i, "is even")
    else:
        print(i, "is odd")
#18
floor_div = 7 // 3
print("The floor division of 7 by 3 is", floor_div)
int_conversion = int(2.7)
print("The integer conversion of 2.7 is", int_conversion)
if floor_div == int_conversion:
    print("The floor division result is equal to the integer conversion")
else:
    print("The floor division result is not equal to the integer conversion")
#19
print(type('10') == type(10))
print(int('10') == 10)
#20
print(float('9.8') == 9.8)
print(round(9.8) == 10)
#21
hours = int(input("Enter hours: "))
rate_per_hour = float(input("Enter rate per hour: "))
salary = hours * rate_per_hour
print("Your weekly earning is", salary)
#22
num_of_years = int(input("Enter number of years you have lived: "))
days_lived = (num_of_years * 365) * 24 * 60 * 60
print("You have lived for", days_lived, "seconds.")
#23
for n in range(1, 6):        # from 1 to 5
    print(f"{n} 1 {n} {n**2} {n**3}")
#End