from queue import Queue as q
import inspect
import time
from abc import ABCMeta, abstractstaticmethod, abstractmethod
from contextlib import contextmanager

class Foo:
    def show(self):
        print("Hi")
def add_attribute(self):
    self.z = 9




class Queue(q):
    def __repr__(self):
        return f"Queue({self._qsize()})"
    def __add__(self, item):
        self.put(item)
    def __sub__(self, item):
        self.get()

qu = Queue()
qu + 9
qu + 7
qu - 3
print(qu)

# in python classes are actually objects, metaclasses define rules for classes, metaclass defines how a class is created
class Test:
    pass
print(Test)  # class is an object and thus this code is vallid
print(Test()) # instance of class
print(type(Test()))  # class is object, you get __main__.Test
print(type(Test))  # of class type, the metaclass, classes made from type class constructor
# syntax of class calls type class, you can create classes directly from class type




Testing = type('Test', (Foo,), {"x":5, "add_attribute":add_attribute})  # valid class made from test class () super class {} attributes
print(Testing())
t = Testing()
print(t.x)
t.wy = "Hello, World!"
print(t.wy)
t.show()
t.add_attribute()
print(t.z)



class Meta(type):
    def __new__(self, class_name, bases, attrs):
        print(attrs)
        a = {}  # new attribute empty dict
        for name, val in attrs.items():
            if name.startswith("__"):
                a[name] = val
            else:
                a[name.upper()] = val

        print(a)
        return type(class_name, bases, a)  # returns an object class
# name, val in attrs dictionary

# metaclass of dog changed from type to Meta
# attribute module is name, qualname dog x 5 y 8



class Dog(metaclass=Meta):
    x = 5
    y = 8
    def hello(self):
        print('hi')


d = Dog()
print(d.X) # construction modified, need capital X

def func(f):
    def wrapper():
        print('Started')
        f()
        print("Ended")
    return wrapper

def func2():
    print("function 2")

def func3():
    print("function 3")

first = func('Hello')  # functions are objects in python

second = func(func2)
print(second)
second()
x = func(func3)
y = func(func2)
x()
y()
func3 = func(func3)
func3()
func2 = func(func2)
func2()

def decorater1(func):
    def mywrapper(*args, **kwargs):
        print("Start")
        rv = func(*args, **kwargs)
        print("Ended")
        return rv
    return mywrapper

@decorater1
def func4(x, y, z):
    print(x + y + z)
    return 50
x = func4(2, 2, 2)
print(x)

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        rv = func(*args, **kwargs)
        total = time.time() - start
        print("Time:", total)
        return rv
    return wrapper


@timer
def test():
    for i in range(100000):
        pass


test()

class Gen:
    def __init__(self, n):
        self.n = n
        self.last = 0
    def __next__(self):
        return self.next()
    def next(self):
        if self.last == self.n:
            raise StopIteration()

        rv = self.last ** 2
        self.last += 1
        return rv
g = Gen(100)

while True:
    try:
        print(next(g))
    except StopIteration:
        break

def gen(n):
    for i in range(n):
        yield i**2

g = gen(100)
for i in g:
    print(i)

#file = open("file.txt", "r")
#try:
    #file.write("hello")
#finally:
    #file.close()

# context managers always makes sure memory is locked or files are closed
#with open("file.txt", "r") as file:
    #file.write('Hello')


class File:
    def __init__(self, filename, method):
        self.file = open(filename, method)

    def __enter__(self):
        print("Enter")
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"{exc_type}, {exc_val}, {exc_tb} ")  # made to handel errors, you can return true after fixing the error
        print("Exit")
        self.file.close()

with File("file.txt", "w") as f:
    print("Middle")
    f.write("Hello, World!")

# Exit method is always called aswell as enter, even if there is an error

@contextmanager
def file(filename, method):
    print("Enter")
    file = open(filename, method)
    yield file
    file.close()
    print("Exit")
with file("file.txt", "w") as f:
    print("middle")
    f.write("Testing")

class Person:
    def __init__(self, name, age, gender):
        self.__name = name
        self.__age = age
        self.__gender = gender
    @property
    def Name(self):
        return self.__name
    @Name.setter
    def Name(self, value):
        if value == "Bob":
            self.__name = "Default Name"
        else:
            self.__name = value
    @staticmethod
    def mymethod():
        print("Hello, World!")

Person.mymethod()

p1 = Person("Solomon", 15, 'm')
print(p1.Name)

p1.Name = "Bob"
print(p1.Name)
# Setters makes it so you have constraints

p1.mymethod()


# mypy allows for type hinting
def myfunction(myparameter: int) -> str:
    return f"{myparameter + 10}"
def otherfunction(otherparameter: str):
    print(otherparameter)

otherfunction(myfunction(20))  # python still dynamically typed




class IPerson(metaclass=ABCMeta):

    @abstractmethod
    def person_method(self):
        """Interface Method"""

class Student(IPerson):
    def __init__(self):
        self.name = "Basic Student Name"
    def person_method(self):
        print("I am a student")

class Teacher(IPerson):
    def __init__(self):
        self.name = "Basic Teacher Name"

    def person_method(self):
        print("I am a teacher")


class PersonFactory:
    @staticmethod
    def build_person(person_type):
        if person_type == "Student":
            return Student()
        elif person_type == "Teacher":
            return Teacher()
        else:
            print("Invalid Type")
            return -1

if __name__ == "__main__":
    choice = input("What type of person do you want to create?\n")
    person = PersonFactory.build_person(choice)
    person.person_method()

# Factory design pattern allows for specified object creation at runtime

class AnotherPerson(IPerson):
    def person_method(self):
        print("I am a person")

class ProxyPerson(IPerson):
    def __init__(self):
        self.person = AnotherPerson()
    def person_method(self):
        print("I am the proxy functionality")
        self.person.person_method()

# proxt design pattern allows for more encapsulation, it wraps functionality around object creation

p1 = AnotherPerson()
p1.person_method()

p2 = ProxyPerson()
p2.person_method()

# singleton only allows one instance of a class

class IPerson2(metaclass=ABCMeta):
    @abstractmethod
    def print_data():
        """Implement in child class"""


class PersonSingleton(IPerson2):
    __instance = None
    @staticmethod
    def get_instance():
        if PersonSingleton.__instance == None:
            PersonSingleton("Default Name", 0)
        return PersonSingleton.__instance

    def __init__(self, name, age):
        if PersonSingleton.__instance != None:
            raise Exception('Singleton cannot be instantiated more than once')
        else:
            self.name = name
            self.age = age
            PersonSingleton.__instance = self

    @staticmethod
    def print_data():
        print(f"Name: {PersonSingleton.__instance.name}, Age: {PersonSingleton.__instance.age}")

p = PersonSingleton("Solomon", 15)
print(p)
p.print_data()

# composite design pattern allows for tree like design

class IDepartment(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self, employees):
        """Implement in child class"""
    @abstractmethod
    def print_department():
        """ Implement in child class"""


class Accounting(IDepartment):
    def __init__(self, employees):
        self.employees = employees
    def print_department(self):
        print(f"Accounting Department: {self.employees}")


class Devolopment(IDepartment):
    def __init__(self, employees):
        self.employees = employees
    def print_department(self):
        print(f"Development Department: {self.employees}")


class ParentDepartment(IDepartment):

    def __init__(self, employees):
        self.employees = employees
        self.base_employees = employees
        self.sub_depts = []

    def add(self, dept):
        self.sub_depts.append(dept)
        self.employees += dept.employees

    def print_department(self):
        print("Parent Department")
        print(f"Parent Department Base Employees: {self.base_employees}")
        for dept in self.sub_depts:
            dept.print_department()
        print(f"total number of employees: {self.employees}")

dept1 = Accounting(200)
dept2 = Devolopment(170)
parent_dept = ParentDepartment(30)

parent_dept.add(dept1)
parent_dept.add(dept2)

parent_dept.print_department()

