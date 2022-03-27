from timeit import default_timer as timer
from collections import Counter
from collections import namedtuple
from collections import OrderedDict
from collections import defaultdict
from collections import deque
from itertools import product
from itertools import permutations
from itertools import combinations, combinations_with_replacement
from itertools import accumulate
from itertools import groupby
from itertools import count, cycle, repeat
from functools import reduce
import logging
import logging.config
mylist = ["Banana", "Cherry", "Apple"]
print(mylist)
#Lists

mylist2 = [5, True, "Apple"]
print(mylist2)
item = mylist[-1]
print(item)

for i in mylist:
    print(i)
if "Banana" in mylist:
    print("yes")
else:
    print("no")

print(len(mylist2))
mylist.append("lemon")
print(mylist)

mylist2.insert(1, "blueberry")
print(mylist2[1])

item = mylist2.remove("blueberry")
print(mylist2) #prints nothing

mylist3 = [4,3,2,1,0,-1,-2]
item2 = mylist3.sort()
print(mylist3) #Sorts in acending order

new_list = sorted(mylist3)
print(new_list) #Same method as the last

mylist4 = [2] * 3
print(mylist4)# Allowes for 3 twos

a = [1, 2, 3, 4, 5, 6, 7]
b = a[0:3]
print(b)
c = a[::3] #takes every third item
print(c)

list_org = ["apples", 'blueberries', "oranges"]
list_cpy = list_org
#Changes to list_cpy aswell makes changes to list_org, due to the set equality
q = [1, 2, 3, 4, 5, 6]
w = [i*i for i in q] #Sqaures the numbers in q
print(w)

#Tuples, cant be changed after creation, unlike lists.
mytuple = ("Max", 28, "Boston") #for only 1 item in tuple leave a comma at the end.
print(mytuple)
eye = mytuple[0]
print(eye)
for i in mytuple:
    print(i)
#If statements and other code that can be used on lists can be used for tuples aswell.
#Dictionaries are collection data type, it is unordered.
mydict = {"name": "Max", "age": 28, "City": "New York"}
print(mydict)
mydict["Email"] = "max@xyz.com" #Added keyvalue
print(mydict)
if "name" in mydict:
    print(mydict["name"])
try:
    print(mydict["wealth"])
except:
    print("Error")
for key, value in mydict.items():
    print(key, value) # Prints out everything wihtout {}
mydict_cpy = mydict
#Changes to mydict_cpy are changes to the original mydict. Due to the set equality.
mydict_cpy2 = dict(mydict_cpy)
#Changes to mydict_cpy2 wont change the orignal copy, since we are using dict()
#You can have 2 dictionarories of different keys, to combine you make use dict.update, then
#Reffer to the dictionary you want to pull from

dict = {3: 9, 6: 36, 9: 81}
print(dict)
value = dict[3] #Prints third term starting from index 0
print(value)
#Sets are unordered, with no duplicates allowed.
myset = {1, 2, 3, 4, 3, 3, 3}
print(myset)
myset2 = set()#Empty set
myset2.add(1)
myset2.add(2)
print(myset2)
for i in myset2:
    print(i)
if 2 in myset2:
    print("yes")
else:
    pass

odds = {1, 3, 5, 7, 9}
evens = {0, 2, 4, 6, 8}
primes = {2, 3, 5, 7}
u = odds.union(evens) #Combines elements from 2 sets without duplication.
print(u)

i = odds.intersection(evens)
print(i) #An empty set is printed due to evens not sharing numbers with odd numbers.

setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setB = {1, 2, 3, 10, 11, 12}
diff = setB.difference(setA)
print(diff) #Prints out whats in A that isnt in B
diff2 = setB.symmetric_difference(setA)
print(diff2)#Prints whats in one set and not in the other.
setA.update(setB)
print(setA) #Adds in the values in setB
setA.intersection_update(setB)
print(setA) #only prints what is found in both, since setA has been updates, it has setB numbers
setA.symmetric_difference_update(setB)
print(setA) #produces an empty set, it elimates what is found in both leaving onyl whats unique, due to previous code it elimates everything leavin onyl an empty set.

setC = {1, 2, 3, 4, 5, 6}
setD = {1, 2, 3}
print(setC.issuperset(setD))
print(setD.issubset(setC)) #Both statements are true as each respective set either has more than the other, or less than the other with some shared elements.
setE = {1, 2, 3, 4, 5, 6}
setF = setE.copy()
setE.add(7)
print(setE)
print(setF) #original set unaffected as the copy method was used.
one = frozenset([1, 2, 3, 4])
print(one) #Frozen set cannot be changed
#Ended at 58:44, String.
#Strings are text representations, theyre ordered. They are immutable, they can't be changed.

my_string = "Hello World"
print(my_string)
char = my_string[::-1] #::-1 would reverse the word.
print(char)
greeting = "Hello"
name = "Tom"
sentance = greeting + " " + name
print(sentance)
for i in greeting:
    print(i)
if 'e' in greeting:
    print("yes")
else:
    print('no')
my_string = "      Hello World       "
print(my_string)
my_string = my_string.strip() #Gets rid of white space.
print(my_string)
print(sentance.upper()) #upper are useful for user input.
print(sentance.replace("Tom", "Jerry"))
my_string = "how are you doing"
my_list = my_string.split() #analyzises for spaces and seperates elements.
print(my_list) #You can join strings with lists.

my_string = "how,are,you,doing"
my_list = my_string.split(",")
print(my_list)
new_string = " ".join(my_list)
print(new_string)

my_list = ["a"] * 1000000

#bad
start = timer()
my_string = ""
for i in my_list:
    my_string += i
stop = timer()
print(stop-start)
#good
start = timer()
my_string = "".join(my_list) #Way of joining elements to empty string
stop = timer()
print(stop-start) #proof that the bad way takes longer.

var = "Tom"
my_string = "the variable is %s" %var #for string use s for int use d, for float use f. .2f would give 2 digits after decimal point for float
print(my_string)

#collections
a = "aaaabbbccc"
my_counter = Counter(a)
print(my_counter)  # Counts the number of unique elements in a string.
print(my_counter.most_common(2))  # two most common types of elements


print(my_counter.most_common(2))  # two most common types of elements
Point = namedtuple("Point", "x,y")
pt = Point(1, -4)
print(pt)
print(pt.x, pt.y)
ordered_dict = OrderedDict()
ordered_dict['a'] = 1
ordered_dict['b'] = 2
ordered_dict['c'] = 3
ordered_dict['d'] = 4
print(ordered_dict)  # Dictionary ordered in order of what is written.

d = defaultdict(int)  # Can be float
d['a'] = 1
d['b'] = 2
print(d)
print(d['a'])

d = deque()
d.append(1)
d.append(2)
d.appendleft(3)
print(d)
d.pop()
print(d)
d.popleft()
print(d)

d.extend([4, 5, 6])
d.extendleft([10,11,12])
print(d)

d.rotate(1)
print(d)
d.rotate(2)
print(d)
d.rotate(-1)
print(d)  # Rotates elements to the right based on the inputed number.
# Ended at 1:37:04, itertools.

a = [1, 2]
b = [3, 4]
prod = product(a, b)
print(list(prod))
prod = product(a, b, repeat=2)
print(list(prod))
a = [1, 2, 3]
perm = permutations(a)
print(list(perm))  # lists the numbers in all possible ways
a = [1, 2, 5, 3, 4]
comb = combinations(a, 2)
print(list(comb))  # All possible combinations with length 2.
comb_wr = combinations_with_replacement(a, 2)
print(list(comb_wr))
acc = accumulate(a)
print(a)
print(list(acc))  # Sums up terms within the list and places the sum.
acc = accumulate(a, func=max)
print(list(acc))
a = [1, 2, 3, 4]
def smaller_than_3(x):
    return x < 3


group_obj = groupby(a, key=lambda x: x<3)
print(group_obj)
for key, value in group_obj:
    print(key, list(value))
persons = [{'name': 'Tim', 'age': 25}, {'name': 'Dan', 'age': 25},
           {'name': 'Lisa', 'age': 27}, {'name': 'Claire', 'age': 28}]
group_obj = groupby(persons, key=lambda x: x['age'])
for key, value in group_obj:
    print(key, list(value))
for i in count(10):
    print(i)
    if i == 15:
        break
a = [1, 2, 3]
for i in cycle(a):
    print(i)
    break
for i in repeat(1, 4):
    print(i)
# Lambda arguments: expression
add10 = lambda x: x + 10  # Creates function with input x, with x it increments it by 10.
print(add10(5))
def add10_func(x):
    return x + 10  # Exact same code as lambda function
mult = lambda x,y: x*y
print(mult(2, 7))  # Lambda functions useful for functions with function parameters.
points2D = [(1, 2), (15, 1), (5, -1), (10, 4)]
points2D_sorted = sorted(points2D)
print(points2D)
print(points2D_sorted)
points2D_sorted = sorted(points2D, key=lambda x: x[1])
print(points2D)
print(points2D_sorted)
def sort_by_y(x):
    return x[1]
points2D_sorted = sorted(points2D, key=sort_by_y)
print(points2D)
print(points2D_sorted)
# map(func, seq)
a = [1, 2, 3, 4, 5]
b = map(lambda x: x*2, a)
print(list(b))
c = [x*2 for x in a]
print(c)
# filter(func, seq)
a = [1, 2, 3, 4, 5, 6]
b = filter(lambda x: x % 2 == 0, a)
print(list(b))
c = [x for x in a if x % 2 == 0]
print(c)
# reduce(func, seq)
a = [1, 2, 3, 4, 5, 6]
product_a = reduce(lambda x,y: x*y, a)
print(product_a)  # Multiplies term to the last element
# Errors and Exceptions
# Syntax errors are errors made in writing the code, not logic. Type errors are errors with data types, like multiplying an int with a string
# There are also import errors, from importing non-existent libraries.
# File not found errors from accessing files that don't exist
# Value errors come from changing or accessing a value that isn't present.
# You can create exceptions with raise exception when some parameter is true.
# Try excepts may let you try something, if it doesn't work except would allow a different code to be run.
# You can create classes that represent custom exceptions.
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(name)s - %(levelname)s - %(message)s',
                    datefmt='%m/%d/%y %H:%M:%S')
logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')

logger = logging.getLogger(__name__)
stream_h = logging.StreamHandler()  # Create handler
file_h = logging.FileHandler('file.log')
# Level and the format
stream_h.setLevel(logging.WARNING)
file_h.setLevel(logging.ERROR)
formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
stream_h.setFormatter(formatter)
file_h.setFormatter(formatter)
logger.addHandler(stream_h)
logger.addHandler(file_h)

logger.warning("This is a warning")
logger.error('this is an error')




