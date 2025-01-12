# import math 
# import custom_math
from custom_math import double as custom_math_double

from math import ceil, floor, sqrt

num = 20.89

print(ceil(num))
print(floor(num))
print(sqrt(num))
print(custom_math_double(num))

from werkzeug.security import generate_password_hash 
from package_math.algebra import add 
from package_math.geometry import square_area


hashed_pass = generate_password_hash("123")
print(hashed_pass)

print(add(2,9))
print(square_area(2))

# random
import random 
value = random.random()
print(value)
value = random.uniform(1, 10)
print(value)
value = random.randint(1, 10)
print(value)

names = ["Tom", "Zoé", "Yanis", "Nora", "Chloé"]
value = random.choice(names)
print(value)
value = random.choices(names, k=10)
print(value)
value = random.choices(names, weights=[1,2,2,1,15] ,k=10)
print(value)

deck = list(range(1, 53))
print(deck)
random.shuffle(deck)
print(deck)
hand = random.sample(deck, k=5)
print(hand)

# uuid 
import uuid 
unique_id = uuid.uuid4()
print(unique_id)

# html 
import html 
unsafe_html = '<script>alert("Vous avez été hacké!");</script>'
safe_text = html.escape(unsafe_html)
print(safe_text)

# xml 
import xml.etree.ElementTree as ET 
tree = ET.parse("data.xml")
root = tree.getroot()

for user in root.findall("user"):
    name = user.find("name").text
    print(f"Nom : {name}")

# json 
import json
original_users = """
{
    "user": [
        {
        "name":"Tom",
        "phone": "+33 6 77 77 77 77",
        "emails": ["tom@mail.com", "tom@mail.fr"],
        "verified": false
        },
        {
        "name":"Paul",
        "phone": "+33 6 44 44 44 44",
        "emails": null,
        "verified": true
        }
    ]
}
"""
data = json.loads(original_users)
print(data)

for user in data["user"]:
    del user["phone"]

new_users = json.dumps(data, indent=2, sort_keys=True)
print(new_users)

#urllig
from urllib.request import urlopen
url = "https://jsonplaceholder.typicode.com/posts"
response = urlopen(url)
data = json.loads(response.read())
print(data)
response.close()

# requests (module externe)
import requests 
response = requests.get(url)
data = response.json()
print(data)

# logging
import logging
logger = logging.getLogger("mylogger")
logger.setLevel(logging.DEBUG)

console_handler = logging.StreamHandler()
console_formatter = logging.Formatter("%(levelname)s : %(message)s")
console_handler.setFormatter(console_formatter)

file_handler = logging.FileHandler("example.log")
file_formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(message)s")
file_handler.setFormatter(file_formatter)
file_handler.setLevel(logging.ERROR)


logger.addHandler(console_handler)
logger.addHandler(file_handler)

def divide(x,y):
    try:
        result = x / y 
    except ZeroDivisionError as e: 
        logger.error("Tentative de division par zéro")
    else:
        return result 

num1 = 20 
num2 = 0
result = divide(num1, num2)
logger.debug(f"Division : {num1} / {num2} = {result}")
logger.info(f"Division : {num1} / {num2} = {result}")
logger.warning(f"Division : {num1} / {num2} = {result}")

# argparse
import argparse 
from package_math.geometry import rectangle_area

def calculate_area(shape, dimensions):
    result = None 
    if shape == "rectangle":
        result = rectangle_area(dimensions[0], dimensions[1])
    elif shape == "square":
        result = square_area(dimensions[0])
    print(result)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Calcule la surface d'une forme en fonctions de ses dimensions"
    )

    parser.add_argument(
        "-s", "--shape",
        required=True,
        choices=["square", "rectangle"],
        metavar="Forme",
        help="Forme de la surface (square ou rectangle)"
    )

    parser.add_argument(
        "-d", "--dimensions",
        required=True,
        type=float,
        nargs="+",
        metavar="Dimensions",
        help="Dimensions de la forme, 1 nombre pour le carré, 2 nombres pour le rectangle"
    )

    args = parser.parse_args()
    calculate_area(args.shape, args.dimensions)