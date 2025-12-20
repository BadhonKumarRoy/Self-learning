#level1
#1
import random
import string
def random_user_id(l=6):
    length = l
    characters = string.digits + string.ascii_letters + string.digits
    user_id = ''.join(random.choice(characters) for _ in range(length))
    return user_id
print(random_user_id())
print(random_user_id())
#2
def user_id_gen_by_user():
    length = int(input("Enter the length of the user ID: "))
    count = int(input("Enter the number of user IDs to generate: "))
    for _ in range(count):
        print(random_user_id(length))
user_id_gen_by_user()
#3
def rgb_color_gen():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return f"rgb({r}, {g}, {b})"
print(rgb_color_gen())
#level2
#1
def list_of_hexa_colors(n):
    hexa_colors = []
    for _ in range(n):
        color = '#' + ''.join(random.choice('0123456789ABCDEF') for _ in range(6))
        hexa_colors.append(color)
    return hexa_colors
print(list_of_hexa_colors(3))
#2
def list_of_rgb_colors(n):
    rgb_colors = []
    for _ in range(n):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        rgb_colors.append(f"rgb({r}, {g}, {b})")
    return rgb_colors
print(list_of_rgb_colors(3))
#3
def generate_colors(color_type, n):
    for _ in range(n):
        if color_type == 'hexa':
            print(list_of_hexa_colors(n))
            return
        elif color_type == 'rgb':
            print(list_of_rgb_colors(n))
            return
generate_colors('hexa', 2)
generate_colors('rgb', 2)
#level3
#1
def shuffle_list(lst):
    random.shuffle(lst)
    return lst
print(shuffle_list([1, 2, 3, 4, 5]))
#2
def seven_random_numbers():
    random_numbers = set()
    while len(random_numbers) < 7:
        random_numbers.add(random.randint(0, 9))
    return list(random_numbers)
print(seven_random_numbers())
print(seven_random_numbers())
print(seven_random_numbers())
print(seven_random_numbers())
#The end