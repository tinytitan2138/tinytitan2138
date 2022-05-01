# Dunder referes to double underscore such as __init__
from queue import Queue as q
import inspect
import math
import time
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __del__(self):
        print('Object deleted')


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __repr__(self):
        return f"X: {self.x}, Y: {self.y}"

    def __len__(self):
        return int(math.sqrt(self.x**2 + self.y**2))

    def __call__(self, *args, **kwargs):
        print('Caller activated')

p = Person('mike', 25)  # triggers init method need not call init method
del p  # deletees object p dunder methods automatically called as class is referenced

v1 = Vector(10, 20)
v2 = Vector(50, 60)
v3 = v1 + v2
print(f"the elements are {v3.x}, {v3.y}")  # may add in division and multiplaction methods
print(v3)
print(len(v3))
v3()


def mydecorater(func):
    def wrapper(*args, **kwargs):
        print('start')
        func(*args, **kwargs)

        print('end')
        val = func(*args, **kwargs)
        return val

    return wrapper

@mydecorater
def helloworld():
    print('hello world')

# mydecorater(helloworld)()

# helloworld()

@mydecorater
def greeting(name):
    print(f"hello, {name}")
    return name.upper()


print(greeting("solomon"))

# logging
def logged(func):
    def wrapper(*args, **kwargs):
        value = func(*args, **kwargs)
        with open('logfile.txt', 'a+') as f:
            fname = func.__name__
            print(f"{fname} returned value {value}")
            f.write(f"{fname} returned value {value}\n")
        return value
    return wrapper

@logged
def add(x, y):
    return x + y

print(add(2, 3))

def timed(func):
    def wrapper(*args, **kwargs):
        before = time.time()
        value = func(*args, **kwargs)
        after = time.time()
        fname = func.__name__
        print(f"{fname} took {after-before} seconds to execute")
        return value
    return wrapper

@timed
def myfunction(x):
    result = 1
    for i in range(x):
        result *= i
    return result


myfunction(10000)
# useful decorater for measuring performence

# seq 1 to 9,000,000
def mygen(x):
    for i in range(x):
        yield x**2

test = mygen(100)
limit = 0
for i in test:
    limit = limit + i
    print(limit)

a = [1, 2, 3]
b = [4, 5]
print(a + b)
print(len(a))
# datatypes like lists are actually objects

class Human:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return f"Human({self.name})"
    def __mul__(self, x):
        if type(x) is not int:
            raise Exception("No int")
        self.name = self.name * x
    def __call__(self, y):
        print("called this function", y)
    def __len__(self):
        return len(self.name)



person1 = Human('Solomon')
print(person1)  # memory address location if no __repr__ method
person1 * 3
print(person1)
person1(1)  # calls the call method
print(len(person1))  # outputs 21 because name was multiplied by 3 via the __mul__ dunder method

q = q()
print(q)

#print(inspect.getsource(q))

class Queue(q):
    def __repr__(self):
        return f"Queue({self._qsize()})"
    def __add__(self, item):
        self.put(item)


qu = Queue()
qu + 3
print(qu)
print('Testing')