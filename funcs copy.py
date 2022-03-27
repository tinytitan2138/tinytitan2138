import copy


def print_name(name):
    print(name)
print_name('Alex')

def foo(a, b, c, d=4):
    print(a, b, c, d)

foo(a=1, c=2, b=3)  # Key words arguments, order doesnt matter. You can combine positional arguments with keywords
foo(1, 2, c=3)  # Keywords arguments are more readable and clear.
foo(1, 2, 3, d=10)

# *args in paremeters allows any number of positional arguments to function
# **kwargs allows any number of key word arguments as arguments,
# They don't need to be called args and kwargs.
# Args is a tuple within a function
# kwargs is a dictionary. Thus you print value for dictionary entry, kwargs[key]
def loo(a, b, *args, **kwargs):
    print(a, b)
    for arg in args:
        print(arg)
    for key in kwargs:
        print(key, kwargs[key])
loo(1, 2, 3, 4, 5, 6, 7, six=6, seven=7, eight=8)
# multiple positional arguments passed in, with key words also passed in
# the key word arguments are dictionaries so it shows definition for key
def zoo(a, b, *, c, d):
    print(a, b, c, d)

zoo(1, 2, c=3, d=4)  # Every argument after star must be passed in as a keyword argument
my_list = [1, 2, 3]
def test(a, b, c):
    print(a, b, c)
my_list = [1, 2, 3]
test(*my_list)
my_tuple = (1, 2, 3)
test(*my_tuple)
my_dict = {'a': 1, 'b': 2, 'c': 3}
test(**my_dict)  # To unpack dictionary, make sure key words in dictionary match the name of the paramter

def test2():
    global number
    x = number
    number = 3
    print('The number  inside the function: ', x)

number = 0
test2()
print(number)

def test3(a_list):
    a_list.append(4)
test3(my_list)
print(my_list)
# Mutable objects can be modified within a function.
result = 5 * 7
print(result)
result = 2 ** 4
print(result)
zeros = [0, 1] * 10
print(zeros)
zeros = (1, 2) * 10
print(zeros)
zeros = 'AB' * 10
print(zeros)

def harmonic_series(boolean):
    n = 1
    s = 1/n
    while boolean == True:
        yield s
        n = n + 1
        s = 1/n
# Harmonic series diverges, numbers
# Cycle through 1 and 9 as first decimal point

# start = True
# series = harmonic_series(start)

# for i in series:
    # print(i)
my_tuple = (1, 2, 3)
my_set = {4, 5, 6}
new_list = [*my_tuple, *my_set]
print(new_list)

org = 5
cpy = org
cpy = 6
print(cpy)
print(org)

org = [0, 1, 2, 3, 4]
cpy = org
cpy[0] = -10
print(cpy)
print(org)  # Change to cpy affects org b/c it's not an actual copy

org = [0, 1, 2, 3, 4]
cpy = copy.copy(org)
cpy[0] = -10
print(cpy)
print(org)  # Copy module allows us to make actual copies

org2 = [[0, 1, 2, 3, 4], [5, 6, 7, 8, 9]]
cpy2 = copy.copy(org2)
cpy2[0][1] = -10
print(cpy2)
print(org2)  # Changes made to both, because shallow copy is 1 level deep


org2 = [[0, 1, 2, 3, 4], [5, 6, 7, 8, 9]]
cpy2 = copy.deepcopy(org2)
cpy2[0][1] = -20
print(cpy2)
print(org2)  # Deep copy fixes the issue

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
p1 = Person('Alex', 27)
p2 = copy.copy(p1)

p2.age = 28
print(p2.age)
print(p1.age)

class Company:
    def __init__(self, boss, employee):
        self.boss = boss
        self.employee = employee
boss = Person('Mike', 55)
employee = Person('Joe', 27)

company = Company(boss, employee)

company_clone = copy.deepcopy(company)
company_clone.boss.age = 56
print(company_clone.boss.age)
print(company.boss.age)
# Deep copy needed for deeper structure. 
