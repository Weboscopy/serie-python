# list 
users = ["Tom", "Zoé", "Sara", "Chloé"]
mylist = list([1, "tom@mail.com", True])
empty_list = []

print(users[0])
print(users[-1])
print(users[0:2])
print(users[:2])
print(users[:-1])
print(users[::2])
print(users[::-1])
print(users.index("Sara"))
print("Zoé" in users)

users.append("Elsa")
print(users)
users.extend(["Mia", "Nora"])
print(users)
users += ["Adam", "Jade"]
print(users)
users.insert(1, "Yanis")
print(users)

users[2:2] = ["Alex", "Julie"] # insetion 
print(users)
users[1:3] = ["Anna", "Nora"] # remplacer
print(users)

users.pop()
print(users)
users.remove("Anna")
print(users)
del users[0]
print(users)

mylist.clear()
print(mylist)

users.sort()
print(users)
users[0] = "adam"
users.sort(key=str.lower)
print(users)
users.reverse()
print(users)

print(sorted(users)) # crée une copie de la liste users

for item in users:
    print(item)

for index, item in enumerate(users):
    print(index, item)

users_string = ','.join(users)
print(users_string)


# tuple
black = (255, 255, 255)
# black[0] = 32
(red, *rest) = black 
print(red, rest)
(red, *green, blue) = black 
print(red, green, blue)
white = tuple((0,0,0))
print(black.count(255))
print(white*3)

names = ["Alice", "Zoé", "Yanis"]
scores = [20, 30, 12]
results = list(zip(names, scores))
print(results)
for name, score in results:
    print(name, score)

color = {"red" : 120, "green": 20, "blue" : 139}
color["red"] = 222
print(color)
from collections import namedtuple
Color = namedtuple("Color", ["red", "green", "blue"])
color = Color(66, 120, 88)
color = Color(red=66, green=120, blue=88)
# color[0] = 20
print(color[0])
print(color.red)


# set 
myset = {1,2,3,4,4,4}
print(myset)
myset2 = set((1,2,3,4,4))
empty_set = set()

nums_list = [2,4,1,8,8,7,7,1,1,1,1]
nums_set = set(nums_list)
print(nums_set)

original_list = [1,2,3,4,4,4,8]
unique_list = list(set(original_list))
print(unique_list)

print(min(nums_set))
print(max(nums_set))
print(sum(nums_set))
print(sum(nums_list))
print(3 in nums_set)

nums_set.remove(2)
# nums_set.remove(3)
nums_set.discard(3)

nums_set.add(9)
others = {3,5}
nums_set.update(others)
print(nums_set)

a = {1,2,3}
b = {4,5,6}
c = a.union(b)
c = a | b 
print(c)

a = {1,2,3}
b = {2,3,4}
c = a & b 
print(a.intersection(b))

print(a.difference(b))
c = a - b

print(a.symmetric_difference(b))
c = a ^ b 

a.symmetric_difference_update(b)
print(a)

# dictionnaire
post = {"id" : 1, "author": "Tom", "published" : True}
product = dict(name="T-shirt", price=20)
empty_dict = {}
print("title" in post)

keys = list(post.keys())
values = list(post.values())
items = list(post.items())
print(keys)
print(values)
print(items)

for key, val in post.items():
    print(f"{key} : {val}")

print(post.get("published"))
print(post["author"])

post["author"] = "Yanis"
print(post)
post.update({"author" : "Zoé", "published" : False})
print(post)

post.popitem()
print(post)
del post["author"]
print(post)

students = {"Tom": 9, "Zoé": 7, "Alice": 7, "Yanis": 9, "Nora": 8, "Sara": 8, "Matteo": 7}
scores = list(students.values())

for score in set(scores):
    num = scores.count(score)
    print(f"{num} élèves ont obtenu {score}")

