
def original_func(name):
    print(f"Salut {name}")


original_func("Zoé")

from datetime import datetime

def decorator_func(original_func):
    def wrapper_func(*args, **kwargs):
       print(datetime.now().strftime("%d-%m-%Y %H:%M:%S"))
       return original_func(*args, **kwargs)

    return wrapper_func


decorated_func = decorator_func(original_func)

decorated_func("Tom")



@decorator_func
def original_func(name):
    print(f"Salut {name}")


original_func("Jade")


@decorator_func
def add_10(num):
    print(num + 10)


add_10(20)

# décorateurs avec arguments
def add_prefix(prefix):
    def decorator_func(original_func):
        def wrapper_func(*args, **kwargs):
            print(prefix)
            return   original_func(*args, **kwargs)
        return wrapper_func
    return decorator_func


@add_prefix("[INFO]")
def get_info(msg):
    print(msg)

@add_prefix("[ERROR]")
def get_error(error):
    print(error)

get_info("Un document a été ajouté")
get_error("Une erreur est survenue")

from functools import wraps 

def logger_decorator(original_func):

    @wraps(original_func)
    def wrapper_func(*args, **kwargs):
       result = original_func(*args, **kwargs)
       print(f"{datetime.now()}  - {original_func.__name__} - args : {args} - kwargs : {kwargs}")
       return result 
    return wrapper_func


import time 
def timer_decorator(original_func):
    @wraps(original_func)
    def wrapper_func(*args, **kwargs):
        t1 = time.time()
        result = original_func(*args, **kwargs)
        t2 = time.time() - t1 
        print(f"{original_func.__name__} a mis {t2} à s'exécuter")
        return result 
    return wrapper_func


@timer_decorator
@logger_decorator
def get_user_info(user):
    print(f"Nom : {user["name"]} ; age : {user["age"]}")


get_user_info({"name" : "Tom", "age" : 28}) 


class decorator_class():
    def __init__(self, original_func):
        self.original_func = original_func
    
    def __call__(self, *args, **kwargs):
       print(f"{datetime.now()}  - {self.original_func.__name__} - args : {args} - kwargs : {kwargs}")
       return  self.original_func(*args, **kwargs)
    

@decorator_class
def get_user_info(user):
    print(f"Nom : {user["name"]} ; age : {user["age"]}")

get_user_info({"name" : "Tom", "age" : 28}) 
