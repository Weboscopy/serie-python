def hello():
    print("hello")


hello()
hello()
hello()
hello()
hello()
hello()

# def add(num1, num2):
#     print(num1 + num2)

# add(3, 7)

def add(num1, num2):
   return num1 + num2


result = add(8, 9)

print(result)

# paramètres par défaut

def add_default(num1, num2=2):
    return num1 + num2 


c = add_default(2)
print(c)

# fonctions variadiques

def add_multiple(*args):
    mysem = 0 
    for i in args:
        mysem += i 
    print(mysem)


add_multiple(1,2,3,4,5,6,7)


def say_hello(**kwargs):
    print(f"Salut {kwargs["first"]} {kwargs["last"]}")

say_hello(first="John", last="Lenon")


# composition de fonctions
print(round(abs(float(input(" Entrez un number : ")))))

# fonctions callback

def process_nums(numbers, callback):
    processed = []
    for number in numbers:
        processed.append(callback(number))
    return processed

def square(x):
    return x * x 

def double(x):
    return 2 * x

print(process_nums([1,2,3,4,5], double))

# la portée des variables

name = "Tom"

def get_name():
    name = "John"
    print(name)

get_name()
print(name)

def get_name():
    global name 
    name = "John"
    print(name)

get_name()
print(name)


def get_score():
    score = 20 
    def update_score():
        score = 30
    
    print(score)
    update_score()
    print(score)

get_score()

def get_score():
    score = 20 
    def update_score():
        nonlocal score 
        score = 30
    
    print(score)
    update_score()
    print(score)

get_score()

# closures

def counter(val):
    print(f"Montant initial {val}")
    def decrement():
        nonlocal val 
        val -= 10 
        if(val <= 0):
            print("Votre compteur est vide")
        else:
            print(f"Il vous rest {val} dans votre compteur")

    return decrement

charge = counter(40)

charge()
charge()
charge()
charge()
charge()

# fonctions curry 
def multiply_standard(num1, num2):
    return num1 * num2 

print(multiply_standard(2,3))

def multiply_curry(num1):
    def by(num2):
        return num1 * num2 
    
    return by 


print(multiply_curry(2)(3))

# fonctions partielles 
multiply_by_10 =  multiply_curry(10)

print(multiply_by_10(2))
print(multiply_by_10(3))
print(multiply_by_10(4))
print(multiply_by_10(5))
print(multiply_by_10(6))

# fonctions lambda 
def multiply_lambda(num1):
    return lambda num2 : num1 * num2 

multiply_by_3 = multiply_lambda(3)
print(multiply_by_3(4))
print(multiply_by_3(5))

# fonctions récursives

user = {
    'username': "tom",
    'location': {
        'city': "Rome",
        'coord': {
            'lat': 44.2,
            'lng': 32.1
        }
    },
    'age': 28
}

def get_all_values(d):
    values = []

    for value in d.values():
        if not isinstance(value, dict):
            values.append(value)
        else:
           values.extend(get_all_values(value))

    return values

print(get_all_values(user))