print("Addition(+):")
x = 5 + 3
print("5 + 3 =", x)
print("Subtraction(-):")
y = 5 - 3
print("5 - 3 =", y)
print("Multiplication(*):")
z = 5 * 3
print("5 * 3 =", z)
print("Modulus(%):")
c = 5 % 3
print("5 % 3 =", c)
print("Division(/):")
a = 5 / 3
print("5 / 3 =", a)
print("Exponentiation(**):")
d = 5 ** 3
print("5 ** 3 =", d)
print("Floor Division(//):")
b = 5 // 3
print("5 // 3 =", b)
print("\n")
My_info = {
'first_name':'Badhon',
'middle_name':'Kumar',
'last_name':'Roy',
'country':'Bangladesh'
}
print("Full Name: ",My_info["first_name"], My_info["middle_name"], My_info["last_name"])
print("Country: ",My_info["country"])
print("I am enjoying 30 days of python")

print(type(10)) # int
print(type(9.8)) # float
print(type(4 - 4j)) # complex
print(type('Badhon')) # str
print(type(['Asabeneh', 'Python', 'Finland'])) # list
print(type({'first_name':'Badhon'})) # dict

point1 = (2, 3) # tuple
point2 = (10, 8) # tuple
print("Point1:", point1)
print("Point2:", point2)
distance = ((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2) ** 0.5
print("Distance between Point1 and Point2:", distance)