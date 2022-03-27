# JSON, JavaScript object notation, lightweight data format used for data exchange.
# JSON is used in web applications. 
import json
from json import JSONEncoder
import random
import secrets
import numpy as np
import functools
import sys
person = {"name": "John", "age": 30, "city": "New York", "hasChildren": False,
          "titles": ["engineer", "programmer"]}
personJSON = json.dumps(person, indent=4, sort_keys=True)
# print(personJSON) Converts python object into json data

with open('person.json', 'w') as file:
    json.dump(person, file, indent=4)  # Converts python object to json data
person = json.loads(personJSON)
print(person)  # Converts json data into a python object


class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.age = age
user = User('Max', 27)

def encode_user(o):
    if isinstance(o, User):
        return {'name': o.name, 'age': o.age, o.__class__.__name__: True}
    else:
        raise TypeError('Object of type user is not JSON serializable')

userJSON = json.dumps(user, default=encode_user)
print(userJSON)  # Encodes custom object as json data

class UserEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o, User):
            return {'name': o.name, 'age': o.age, o.__class__.__name__: True}
        return JSONEncoder.default(self, o)
userJSON = json.dumps(user, cls=UserEncoder)
print(userJSON)

userJSON = UserEncoder().encode(user)
print(userJSON)  # Different ways to encode into json data
def decode_user(dct):
    if User.__name__ in dct:
        return User(name=dct['name'], age=dct['age'])
    return dct
# Decodes custom object
user = json.loads(userJSON, object_hook=decode_user)
print(type(user))  # Creates dictionary
print(user.name)
a = random.normalvariate(0, 1)
print(a)
mylist = list("ABDFEFGH")
a = random.choices(mylist, k=3)
print(a)
random.shuffle(mylist)
print(mylist)

random.seed(1)
print(random.random())
print(random.randint(1, 10))
random.seed(1)
print(random.random())
print(random.randint(1, 10))
# Pseudo random numbers. You can reproduce data.
a = secrets.randbelow(10)
print(a)
a = secrets.randbits(4)
print(a)
mylist = list("ABCDEFGH")
a = secrets.choice(mylist)
print(a)

a = np.random.rand(3,3)
print(a)
a = np.random.randint(0, 10, (3,4))
print(a)
arr = np.array([[1,2,3], [4,5,6], [7,8,9]])
print(arr)
np.random.shuffle(arr)
print(arr)
np.random.seed(1)
print(np.random.rand(3,3))
np.random.seed(1)
print(np.random.rand(3,3))

def start_end_decorator(func):
    def wrapper():
        print('Start')
        func()
        print('End')
    return wrapper

@start_end_decorator
def print_name():
    print("Alex")

# print_name = start_end_decorator(print_name)


print_name()
# Extends the behavior of a function. (Decorators)

def start_end_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('Start')
        result = func(*args, **kwargs)
        print('End')
        return result
    return wrapper

@start_end_decorator
def add5(x):
    return x + 5

result = add5(10)
print(result)
print(help(add5))
print(add5.__name__)

def decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Do..
        result = func(*args, **kwargs)
        # Do..
        return result
    return wrapper

@start_end_decorator
def addnum(x):
    return x + 1
# Template for decorators.

def repeat(num_times):
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator_repeat




@repeat(num_times=3)
def greet(name):
    print(f'Hello {name}')

greet('Alex')




def debug(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
        signature = ", ".join(args_repr + kwargs_repr)
        print(f"Calling {func.__name__}({signature})")
        result = func(*args, **kwargs)
        print(f"{func.__name__!r} returned {result!r}")
        return result
    return wrapper


@debug
@start_end_decorator
def say_hello(name):
    greeting = f'Hello {name}'
    print(greeting)
    return greeting

say_hello('Alex')

class CountCalls:
    def __init__(self, func):
        self.func = func
        self.num_calls = 0
    def __call__(self, *args, **kwargs):
        self.num_calls += 1
        print(f'This is executed {self.num_calls} times')
        return self.func(*args, **kwargs)


@CountCalls
def say_hello():
    print('Hello')
say_hello()
say_hello()

def mygenerator():
    yield 1
    yield 2
    yield 3
g = mygenerator()
value = next(g)
print(value)
value = next(g)
print(value)
value = next(g)
print(value)

def countdown(num):
    print('Starting')
    while num > 0:
        yield num
        num -= 1
cd = countdown(4)
value = next(cd)
print(value)
print(next(cd))
print(next(cd))
print(next(cd))

def firstn(n):
    nums = []
    num = 0
    while num < n:
        nums.append(num)
        num += 1
    return nums
print(sum(firstn(10)))

def firstn_generator(n):
    num = 0
    while num < n:
        yield num
        num += 1
print(sum(firstn_generator(10)))

print(sys.getsizeof(firstn(100000)))
print(sys.getsizeof(firstn_generator(100000)))  # Generators good for memory

def fibonacci(limit):
    a, b = 1, 1
    c = b/a
    while a < limit:
        yield c
        a, b = b, a + b
        c = b/a

fib = fibonacci(1000000000)
for i in fib:
    print(i)

mygenerator = (i for i in range(1000000) if i % 2 == 0)  # Generator saves memory
print(sys.getsizeof(mygenerator))
mylist = [1 for i in range(1000000) if i % 2 == 0]

print(sys.getsizeof(mylist))


