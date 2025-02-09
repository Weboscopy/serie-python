# mapping 
double_nums = []
for n in range(1,6):
    double_nums.append(n *2)

print(double_nums)

def double(n):
    return n * 2

double_nums = list(map(double, range(1,6)))
print(double_nums)

double_nums = [double(n) for n in range(1,6)]
print(double_nums)

nums = [1,2,3,4,5]
squares_nums = []
for n in nums:
    squares_nums.append(n*n)

print(squares_nums)

squares_nums = list(map(lambda n : n*n, nums))
print(squares_nums)

squares_nums = [n*n for n in nums]
print(squares_nums)

# filter
prices = [100, 90, 23, 30, 80, 12, 70, 27, 10]

cheap_prices = []
for p in prices:
    if p <= 60:
        cheap_prices.append(p)

print(cheap_prices)

cheap_prices = list(filter(lambda p: p <= 60, prices))
print(cheap_prices)

cheap_prices = [p for p in prices if p <= 60]
print(cheap_prices)
cheap_prices = [p if p <= 60 else "trop cher" for p in prices]
print(cheap_prices)

# any
temperatures = [-4, -1, 0, 12, 10, -8]
has_positive = False 
for temp in temperatures:
    if temp > 0:
        has_positive = True 
        break 

print(has_positive)

has_positive = any(temp > 0 for temp in temperatures)
print(has_positive)

password = "Pass123!"
has_upper = any(char.isupper() for char in password)
print(has_upper)
has_digit = any(char.isdigit() for char in password)
print(has_digit)
import string 
has_special = any(char in string.punctuation for char in password)
print(has_special)

# all
numbers = [1, -2, 3, 4]
all_positive = True 
for num in numbers:
    if num <= 0:
        all_positive = False
        break 

print(all_positive)

all_positive = all(num > 0 for num in numbers)
print(all_positive)

user = {
    "username": "paul",
    "email": "paul@mail.com",
    "age": -2
}

def validate_user(user):
    return all([
        isinstance(user["username"], str) and user["username"].strip() != "",
        isinstance(user["email"], str) and "@" in user["email"],
        isinstance(user["age"], int) and user["age"] > 0 
    ])

print(validate_user(user))
# sort 
grades = [9, 7, 10, 12, 4, 18, 17, 13, 19]

sorted_grades = sorted(grades)

print(sorted_grades)

sorted_grades = sorted(grades, reverse=True)
print(sorted_grades)

print(grades)
grades.sort()
print(grades)

students = [("Yannis", "B"), ("Paul", "C"), ("Zoé", "A")]

sort_by_grade = lambda student : student[1]
sorted_students = sorted(students, key=sort_by_grade)
print(sorted_students)
students.sort(key=sort_by_grade)
print(students)

class Employee:
    def __init__(self, name, age):
        self.name = name 
        self.age = age

    def __repr__(self):
        return f"Employee(name={self.name}, age={self.age})"


e1 = Employee("Tom", 31)
e2 = Employee("Yanis", 26)
e3 = Employee("Zoé", 29)

employess = [e1,e2,e3]
sorted_employees = sorted(employess, key=lambda e: e.age, reverse=True)
print(sorted_employees)
from operator import attrgetter
sorted_employees = sorted(employess, key=attrgetter("age") , reverse=True)
print(sorted_employees)

# reduce 
prices =  [100, 90, 23, 30, 80, 12, 70, 27]
total = sum(prices)
print(total)

import math 
total = math.prod(prices)
print(total)

from functools import reduce 

total = reduce(lambda acc, curr : acc + curr, prices, 0)
print(total)
total = reduce(lambda acc, curr: acc * curr, prices, 1)
print(total)


cart = [
    {"name": "PC", "price": 999.99, "quantity": 1},
    {"name": "Smartphone", "price": 599.99, "quantity": 2},
    {"name": "Tablette", "price": 299.99, "quantity": 1},
    {"name": "Casque audio", "price": 149.99, "quantity": 3},
]


def calculate_total_product(product):
    return product["price"] * product["quantity"]

total_cart = reduce(
    lambda acc, product: acc + calculate_total_product(product),
    cart,
    0
)

print(total_cart)

# enumerate 
usernames = ["Yanis", "Tom", "Zoé"]
for index, username in enumerate(usernames):
    print(f"id {index + 1} - username {username}")

# zip 
passwords = ["Yanis123", "Tom123", "Zoé123"]
emails = ["Yanis@mail.com", "tom@mail.com", "zoe@mail.com"]

users = list(zip(passwords, emails))
print(users)

for user in users :
    print(f"Mot de passe : {user[0]} - Email : {user[1]}")


keys = ["username", "email", "passwords"]
values = ["yanis", "yanis@mail.com", "yanis123"]

user_dict = dict(zip(keys, values))
print(user_dict)

# produits cartésien 
foods = ["Pizza", "Burger", "Sushi"]
beverages = ["Soda", "Juice", "Water"]

menus = []
for food in foods:
    for beverage in beverages:
        menus.append((food, beverage))

print(menus)

import itertools
menus = list( itertools.product(foods, beverages))
print(menus)

menus = [(food, beverage) for food in foods for beverage in beverages]
print(menus)

# set comprehension
numbers = [1,1,2,2,3,4,4,5]

squares_of_evens = {num**2 for num in numbers if num % 2 == 0}
print(squares_of_evens)

# dict comprehension
temp_in_C = {"Paris": 17, "Lyon": 19, "Marseille": 25, "Nice": 30}

temp_in_F = {key : round(value * 9/5 + 32) for key, value in temp_in_C.items()}
print(temp_in_F)

weather = {"Paris" : "nuageux", "Lyon": "Nuageux", "Marseille": "Ensoleillé", "Nice" : "Ensoleillé"}
sunny_weather = {key : value for (key, value) in weather.items() if value == "Ensoleillé"}
print(sunny_weather)

cities_weather = {key : ("Chaud" if value >= 20 else "Froid") for (key, value) in temp_in_C.items()}
print(cities_weather)

def check_temps(temp):
    if temp >= 30:
        return "Chaud"
    elif 20 <= temp <= 25:
        return "Beau temps"
    else:
        return "Froid"

cities_weather = {key : check_temps(value) for (key, value) in temp_in_C.items()}
print(cities_weather)