print("Hello World")
ex_var = 5
# variable is changeable
ex_var = 7

# ex:
# 4callingbirds
# $please.avoid!?
# camelCase
# snake_case_variable
# numb3rsOk4yAfter1st

# variable is dynamically typed
float_1 = 1.2345
int_1 = 7
int_2 = -52
bool_1 = True
bool_2 = False

int_3 = -88
float_3 = 5.986222
bool_3 = True
int_3 = 551

# standard comment
addition = 4 + 5  # 9
subtraction = 5 - 2  # 3
division = 7 / 2  # 3.5
multiplication = 3 * 8  # 24

exponentiation = 4 ** 4  # 256
floor_division = 16 // 5  #
modulo = 7 % 3  # return the rest

add_assign = 5
add_assign += 7  # result = 12
# is like add_assign = add_assign + 7

# subtraction
sub = 10
sub -= 5  # 5
# multiplication
mult = 10
mult *= 5  # 50
# division
div = 10
div /= 5  # 2.0
# exponentiation
exp = 10
exp **= 2  # 100
# floor division
floor = 10
floor //= 6  # 1
# modulo
mod = 10
mod %= 7  # 3

# operator precedence = ()
# **
# % / // *
# + -

expression = (9 - 7) * 2 ** 3 + 10 % 6 // -1 * 2 - 1
print(expression)

example_1 = 3.14159
example_2 = 24601
example_3 = True
example_5 = 10 + 9

print(example_1)
print(example_2)
print(example_3)

print(example_5)
print((4 + 5) * 3)

var_ex = "Word"  # variable definition of string
print(var_ex)  # Print var_ex variable
print(2)  # print number 2 directly
print(5 - 15 / 2)  # print math operation

print(1.23 + 2.80)
ex2 = (123 + 280) / 10
print(ex2)  # approximation
# round()

ex3 = 1.23 + 2.80
print(round(ex3, 2))

# Grocery values
penne = 16.68 * 100
arrabiata_pasta = 6.98 * 100
organic_garlic = 16.78 * 100
italian_seasoning = 15.26 * 100
artisan_baguettes = 3.00 * 100
meatballs = 4.39 * 100

# expression
sub_total = (penne + arrabiata_pasta + organic_garlic + italian_seasoning + artisan_baguettes + meatballs) / 100
print(sub_total)

# Strings
ex_1 = 'This is a string'
ex_2 = "This is also a string"
ex_3 = '1984!'
ex_4 = 'LiVe LONG and PRosPEr.'
ex_5 = "!@#S%^&*()_-=+=/.,?><:;~'|][}{"
ex_6 = ""
ex_7 = "0123456"  # index begins with 0
ex_8 = "orange"
print(ex_8[2])
print("apple"[4])

ex_10 = "apricots"
print(ex_10[:3])  # show all positions before 3 less the 3 in end, so: 0 1 2 (apr)
print(ex_10[2:5])  # show all positions between 2 and 5, less the 5 in end, so 2 3 4 5 (ric)
print(ex_10[4:])  # show all positions after 4, incluind 4, so: 4 5 6 7 (cots)
# left number (before slice) - include it/ right number (after slice) - exclude it
# is possible handle with it like char in C language

# concatenation:
print("pecan" + " " + "pie")

concatenated = "R2" + "-" + "D2"
print(concatenated)
print(concatenated[3])
print(concatenated[1:4])

unchanged = "forrest gump"
sliced = unchanged[6:]
print(sliced)
print(unchanged)
print(unchanged[10])
print(unchanged)

ex_1 = False
ex_2 = 23
ex_3 = 4.1352
ex_4 = str(True)  # convert for string
ex_5 = str(5)
ex_6 = str(3.21)

# Show type of variable
print(type(ex_1))
print(type(ex_2))
print(type(ex_3))
print(type(ex_4))
print(type(ex_5))
print(type(ex_6))

# escape sequence
print("This\tis\ta\tlot\tof\tspace.")  # Tab
print("line one\nline two")  # break line
print('"When I said \'immediately,\'I meant today!" said King Saul.')
print("\"Do or do not. There is no try.\"")
print("All escape sequences contain a \\.")
# \ escapes help to avoid confusion between ' and "

'''
name = input("Please enter your name: ") # Data get in
print("Your name is " + name + ".")
print(type(name))

fav_num = input("What is your favorite number? ")
print("Your favorite number is " + fav_num + ".")
print(type(fav_num))

# int and float
user_int = input("Please enter an integer. ")
print(user_int)
print(type(user_int))

user_float = float(input("Plase enter a float. "))
print(user_float)
print(type(user_float))
'''

print("this")
print("is")
print("an")
print("example")
print("this")
print("is")
print("an")
print("example")
print("this")
print("is")
print("an")
print("example")


def prints_four():
    print("this")
    print("is")
    print("an")
    print("example")


prints_four()
prints_four()
prints_four()
prints_four()
prints_four()


# def = functions (is possible store string or numbers here)
# context = defined by indented
def function_name(parameter):
    print(parameter + 2)


function_name(8)
# Result is 10, because the function received number 8 like a parameter

first_str = "The number "


def function_2(p1, p2, p3):
    print(p1 + str(p2) + p3)


function_2(first_str, 5, " is an integer.")


# called like arguments in parameter

def default_example(num1=7, num2=8):
    # print(num1 * num2)
    print(num1 * num2)


'''
# default_example(2)
# product = default_example(2)
print(default_example() + 44)
'''
# import generic
import random

# call two integers between 1 and 10:
print(random.randint(1, 10))

# function import (import like a module)
from random import randint

print(randint(10, 20))

# universal import
from random import *

# return float number between 0.0 and 1.0
print(random())

# Variable scope
# global (outside functions) and local scope (inside functions)
example_4 = "Hello World"  # global


def loc_ex():
    example_4 = "This is a string"  # local
    return example_4


print(example_4)
print(loc_ex())


def loc_ex2():
    breakfast = "Waffles"
    return breakfast


loc_ex2()


# print(breakfast) # is not defined

def print_glob():
    loc_var = " that is very long."
    print(glob_var + loc_var)


glob_var = "This is a string example"
print_glob()


# Don't have order to access the data (logical order of algorithm)

def first():
    loc = 2
    return loc


def second():
    return  # loc()


first()
second()  # Don't return loc


def loc_ex1():
    global fruit  # called global variable for inside function and define it
    fruit = "pear"
    print(fruit)


def loc_ex2():
    fruit = "banana"
    print(fruit)


fruit = "apple"
loc_ex1()
loc_ex2()
print(fruit)

# Comparison Operators: >, <, >=, <=, !=, ==
print(4 > 2)
print(1 > 3)
print(5.79 < 6)
print(3 < 3)
print(9 >= 9)
print(1 <= 2)
print(10 != 100)
print(10 != 10)
print(10 == 100)
print(10 == 10)
print("Hello" == "Hello")
print("Hello" != "World")
print("Hello" == "hello")  # Case sensitive
print(4.0 >= 4)
print(4.0 <= 4)
print(4.0 == 4)
# = (attribution) vs == (equal) / and, or, not

print(4 > 1 or "word" == "word")
print(8.76 == 8.7600 or 2 != 2)
print("earth" == "Earth" or 6 <= 3)
print(10 == 5 or 10 != 5)

print(not 6482 > 0)
print(not "Python" != "Python")
"""
# if Statements
veg = input("Type the name of a vegetable: ")
if veg == "corn":
    print("The vegetable is corn.")
else:
    print("The vegetable is not corn.")
"""

"""
# nested
gpa = float(input("What was the applicant's grade point average? "))
inst_app = input("Is the student going to be educated at an approved institution? ")

if gpa >= 3.7:
    if inst_app == "yes":
        print("The applicant qualifies for a low APR student loan.")
    else:
        print("The applicant does not qualify since they have not been accepted into an approved institution.")
else:
    print("The applicant did not have high enough grades to qualify.")

user_num = int(input("Please enter an integer: "))

if user_num < 0:
    print("The number you entered is less than 0.")
elif user_num == 0:
    print("The number you entered is 0.")
elif 0 < user_num <= 100:
    print("The number you entered can be 1, 100, or anything in between.")
else:
    print("The number you entered is greater than 100.")
"""
"""
# Truthy and falsey values
strings_example = input("Enter any string other than an empty one: ")

if strings_example != "":
    print("Thank you for entering something.")
else:
    print("You did not enter a string.")
"""
# bool if is different than 0, so it's true.
print(bool(0))
print(bool(400))
print(bool(0.0))
print(bool(3.14159))
print(bool(""))
print(bool("Hello world"))

# While loops
counter = 0
while counter < 3:
    print("Something")
    counter += 1

counter = 1
while counter < 6:
    print(counter)
    counter += 1

# Infinite loops
counter = 1
while counter < 9:
    print(counter)
    counter = counter + 1

word = "house"
for letter in word:
    print(letter)

# Range
one_input = range(5)

for num in one_input:
    print(num)

# Calling ranges
two_inputs = range(5, 10)

for num in two_inputs:
    print(num)

three_inputs = range(1, 20, 3)
# first number/ last number/ interval
for num in three_inputs:
    print(num)
# Range = one less than informed, if is 20 (for example), last number is 19.

# String methods
all_low = "there are no capitals here."
print(all_low.upper())
print(all_low)
all_up = "THERE IS SHOUTING TEXT!"
print(all_up.lower())
print(all_up)

print("Mixed Case".isupper())
print("ALL CAPS".isupper())
print("AAAHHHH!".islower())
print("$100 is a lot to make in an hour.".islower())
print("".isupper())
print("37&8.,?:\"".islower())
print("SHOUT!".lower().isupper())
print("Batman123".isalnum())
print("Batman".isalnum())
print("123".isalnum())
print("123".isdecimal())
print("3.14".isdecimal())
print(" ".isspace())
print("                  ".isspace())
print("not just spaces".isspace())
print("not just spaces"[3].isspace())
print("The Empire Strikes Back".istitle())  # Title case
print("Super Smash Brothers: Ultimate!".istitle())
print("the great gatsby".title())  # Convert
print("this is a string".startswith("T"))
print("To infinity and beyond!".endswith("!"))
print("".join(["one", "two", "three"]))
print(" ".join(["one", "two", "three"]))
print(",".join(["one", "two", "three"]))
print(", ".join(["one", "two", "three"]))
print("...".join(["one", "two", "three"]))
print("Eggs, Milk, Waffles, Bacon".split(","))

print("hello world".rjust(15))
print("hello world".ljust(15) + "four spaces later.")
print("hello world".rjust(15, "-"))
print("hello world".ljust(15, "*"))
print('hello world'.center(15, ":"))
print("I had an exciting trip!!!11111")
print("I had an exciting trip!!!11111".strip("1"))
print("I had an exciting trip!!!11111".rstrip("1"))
print("I had an exciting trip!!!11111".lstrip("1"))
print("juice, bread, cheese, beef, bread.".rstrip(",ed arb"))
print("blueblueyellowblue".strip("eulb"))
print("Good morning.".replace("morning", "afternoon"))

# Len
print(len("tree"))
print("This" + " " + "is a " + "string.")
print(len("This" + " " + "is a " + "string."))
print("antidisestablishmentarianism"[7:20])
print(len("antidisestablishmentarianism"[7:20]))

# Format
"""
name = input("What is the job applicant's name? ")
degree = input("What did they major in at college? ")
job = input("What is their current occupation? ")
experience = input("How many years have they been working in their field? ")

print(name + " majored in " + degree + ", works as a " + job + ", and has " + experience + " years of experience.")

# {} substitute of variables
print("{} majored in {}, works as a {}, and has {} years of experience.".format(name, degree, job, experience))
"""
# List
example_list_1 = [5, 4, 3, 2, 1]
example_list_2 = [2.718, 9.31]
example_list_3 = ["blue", "green", "red", "yellow", "purple", "orange"]
example_list_4 = [True, False, False, True, False, True, True, False, True]
example_list_5 = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
example_list_6 = [10, 3.14159, "tree", False, [1, 2, 3]]

print(list("blah"))
checked_list = [1, 2, 3, 4]
not_in_example = 3 not in checked_list
print(not_in_example)

# index and list
indexes_example = ["carpet", "hardwood", "linoleum"]
print(indexes_example[2][0])
indexes_example2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(indexes_example2[2][0])  # it's third list, position zero

negative = [1, 2, 3, 4, 5]
print(negative[-1])
print(negative[-2])
print(negative[-3])
print(negative[-4])
print(negative[-5])

mixed = [False, 365, 4.24, "this is a string"]
print(mixed[2] + 1.76)
print("I have used \"" + mixed[-1] + "\" as an example too many times.")

# list slicing
sliced = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(sliced[:4])
print(sliced[3:8])
print(sliced[6:])

example = [2, 4, 6, 8, 0]
print(example)
example[3] = 10
print(example)
example[4:7] = [7, 6, 5]
print(example)

# del and list
planets = ["pluto", "mars", "earth", "venus"]
del planets[0]
print(planets)
planets.remove("mars")
print(planets)
colors = ["blue", "red", "white", "blue", "orange", "blue"]
colors.remove("blue")
print(colors)
pets = ["cat", "dog", "parrot"]
print(pets)
pets.append("fish")
print(pets)
pets.insert(1, "turtle")  # insert in specific position
print(pets)
num_list = [2.718, 4, -19, 10000, 0]
print(num_list)
num_list.sort()
print(num_list)  # random position
str_list = ["Ringo", "John", "George", "Paul"]
print(str_list)
str_list.sort()
print(str_list)
num_list.sort(reverse=True)
print(num_list)
str_list.sort(reverse=True)
print(str_list)
mixed = [False, 5.67, -2]
mixed.sort()
print(mixed)

# ASCIIbetical order
ASCIIbetical = ["Andy", "kiwi", "apple", "Karen", "Brian", "banana"]
ASCIIbetical.sort(key=str.lower)  # In orders typed
print(ASCIIbetical)
metals = ["cooper", "gold", "silver", "iron"]
print(metals.index("silver"))
numbers = [4, 3, 2, 1, 0, 1, 2, 3, 4]
print(numbers.index(3))
bands = ["Queen", "Led Zeppelin", "The Beatles", "MUSE", "Radiohead"]
end = bands.pop(3)
print(bands)
print(end)

# Lists and strings
ex_1 = [1, 2, 3]
ex_1[1] = 5  # reassignment
print(ex_1)
ex_2 = "123"
# ex_2[1] = 5
print(ex_2)

ex_3 = "No, you can't."
ex_4 = "Yes" + ex_3[3:11] + "!"
print(ex_4)
ex_5 = 3.14
ex_6 = "coconut"
ex_7 = ex_5
ex_8 = ex_6
print(ex_7)
print(ex_8)
ex_9 = [1, 2, 3, 4, 5]
ex_10 = ex_9
ex_10[2] = 4
print(ex_9)
print(ex_10)
# copy and deepcopy
import copy

ex_12 = [1, 2, 3, 4, 5]
ex_13 = copy.deepcopy(ex_12)
ex_13[2] = 4
ex_14 = ex_13
ex_14[4] = 6
print(ex_12)
print(ex_13)
ex_15 = ["bush",
         "fern",
         "tree",
         "moss"]
print(ex_15)
ex_16 = 2 + \
        4 + \
        1
print(ex_16)

ex_17 = "The Emp\
ire Strikes\
 Back"
print(ex_17)

ex_18 = "hello " + \
        "world"
print(ex_18)

# dictionaries
consoles = {"nintendo": "wii", "microsoft": "xbox", "sony": "playstation"}
print(consoles["microsoft"])  # key value
val = consoles["microsoft"]
print(val)
print("The " + consoles["sony"] + " 5 is Sony's newest gaming console.")

mohs_hardness = {9: "corondum", 10: "diamond"}
floats = {1.23: 1000, 3.14159: 10000, 2.718: 100000}
mixed = {"string": 1, 10210: 2, 4.976: 3, False: 4}

print([2, 4, 6] == [2, 4, 6])
print([2, 4, 6] == [6, 4, 2])

first = {0: 2.1, 1: 2.2, 2: 2.3, 3: 2.4}
second = {2: 2.3, 0: 2.1, 3: 2.4, 1: 2.2}
print(first == second)
print(0 in first)
print(1 not in first)

birth_years = {1994: "bill", 1969: "emily", 1982: "elizabeth", 2000: "turner"}
print(birth_years.keys())
for key in birth_years.keys():
    print(key)

print(birth_years.values())
for key in birth_years.values():
    print(key)

print(birth_years.items())
for key, value in birth_years.items():
    print(key, value)

print(type(birth_years.keys()))
print(type(birth_years.values()))
print(type(birth_years.items()))

print(list(birth_years.keys()))
print(list(birth_years.values()))
print(list(birth_years.items()))

print("elizabeth" in birth_years.values())

if 1975 in birth_years:
    print(birth_years[1975])
else:
    print("1975 is not a key in birth_years.")

print(birth_years.get(1975, "1975 is not a key in birth_years."))

print(birth_years)
people = birth_years
people[1982] = "madeline"
print(birth_years)

birth_years = {1994: "bill",
               1969: "emily",
               1982: "elizabeth",
               2000: "turner"}
print(len(birth_years))

ex_1 = {}.fromkeys(["address"], "1600 Pennsylvania Avenue NW")
print(ex_1)
ex_1 = {}.fromkeys("addr", "1600 Pennsylvania Avenue NW")  # two keys
print(ex_1)
ex_1 = {}.fromkeys(["brand"])
print(ex_1)

ex_2 = {"make": "Honda", "model": "civic", "year": 2016}
popped = ex_2.pop("model")
print(ex_2)
print(popped)

popped = ex_2.pop("make")
print(ex_2)
print(popped)

ex_3 = {"name": "bob", "age": 38, "occupation": "accountant", "workplace": "H&R block"}
# ex_3.popitem("bob")
print(ex_3)

ex_1 = {1: "England", 2: "Scotland", 3: "Wales", 4: "Northern Ireland"}
print(ex_1)
ex_1.clear()
print(ex_1)

print(birth_years)
people = birth_years
people[1982] = "madeline"
print(birth_years)

city_info = {"country": "Canada", "province": "Ontario", "city": "Toronto"}
population = {"population": 2930000}
city_info.update(population)
print(city_info)
print(population)
city_info["population"] = 3000000
print(city_info)
city_info.update(population)
print(city_info)

computers = {"Google": "ChromeBook", "Apple": "MacBook", "Microsoft": "Surface Pro"}
if "Lenovo" not in computers:
    computers["Lenovo"] = "ThinkPad"
print(computers)

computers.setdefault("Lenovo", "ThinkPad")
print(computers)
computers.setdefault("Lenovo", "IdeaPad")
print(computers)
computers.setdefault("Apple", "MacBook Pro")
print(computers)

empty = dict()
print(empty)
with_values = dict(a=1, b=2, c=3)
print(with_values)

# tuples
tuple_5 = tuple([3.14, 2.205, 10])
tuple_6 = tuple("edcba")
print(tuple_5)
print(tuple_6)

tuple_7 = tuple({"a": 1, "b": 2, "c": 3})
print(tuple_7)

tuple_8 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(tuple_8[2])
print(tuple_8[:8])
print(tuple_8[2:7])
print(tuple_8[3:])
# ERROR = tuple_8[0] = "a"

tuple_9 = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Satuday", "Sunday")
tuple_10 = ("Fall", "Winter", "Spring", "Summer")
tuple_11 = (
'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
'y', 'z')

tuple_12 = (1, 3, 5)
list_1 = [1, 3, 5]
print(tuple_12.__sizeof__())
print(list_1.__sizeof__())

occupations = {("Angus", "Young"): "musician",
               ("Narendra", "Modi"): "prime minister",
               ("Richard", "Branson"): "entrepeneur",
               ("Quentin", "Tarantino"): "filmmaker"}

seven_wonders = {("29°58´44´´N", "31°08´02´´E"): "The Great Pyramid of Giza, Egypt",
                 ("33°13´23´´N", "43°40´45´´E"): "Hanging Gardens of Babylon",
                 ("37°38´18´´N", "21°37´47´´E"): "Archaeological Site of Olympia, Greece",
                 ("37°55´33´´N", "23°59´36´´E"): "Temple of Artemis at Ephesus",
                 ("37°02´16´´N", "27°25´26´´E"): "Mausoleum at Halicarnassus",
                 ("36°26´02´´N", "28°13´03´´E"): "Rhodes, Greece",
                 ("31°12´51´´N", "29°53´28´´E"): "Lighthouse of Alexandria, Egypt", }

major_cities = ("Tokyo", "London", "New York", "Shangai", "Sidney")
count = 0
while count < len(major_cities):
    print(major_cities[count])
    count += 1

backwards = len(major_cities) - 1
while backwards >= 0:
    print(major_cities[backwards])
    backwards -= 1

ints = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(ints[::3])
print(ints[1::2])
print(ints[7::-1])
print(ints[8::-2])

nested = (1, 2, 3, (4, 5, 6), (7, 8, 9), (10, 11, 12))
print(nested[4])
print(nested[5][1])

repeat = (7, 3, 3, 3, 0, 0, 7, 0, 0)
print(repeat.count(7))
print(repeat.count(3))
print(repeat.count(0))

ints2 = (1, 1, 7)
print(ints2.index(7))
print(ints2.index(1))
# print(ints2.index(8)) = is not in tuple

# sets
set_1 = {9, 8, 8, 8, 7, 6}
set_2 = set({"a", "b", "c", "d", "e"})
print(set_1)
print(set_2)
set_3 = set(range(1, 12, 2))
print(set_3)
set_4 = {"a", 3.14, 18, True}
print(set_4)
set_5 = {3, 6, 9, 12, 15}
for num in set_5:
    print(num)

print(12 in set_5)
print(10 in set_5)

olympic_cities = ["Athens", "Paris", "St. Louis", "London", "Stockholm", "Berlin", "Antwerp",
                  "Charmonix", "Paris", "St. Moritz", "Amsterdam", "Lake Placid",
                  "Garmisch-Partenkirchen", "Berlin", "Sapporo Garmisch-Partenkirchen",
                  "Tokyo Helsinki", "Cortina d'Ampezzo", "Melbourne Stockholm", "Squaw Valley",
                  "Rome", "Innsbruck", "Montreal", "Lake Placid", "Moscow", "Sarajevo", "Los Angeles",
                  "Calgary", "Seoul", "Albertville", "Barcelona", "Lillehammer", "Atlanta", "Nagano",
                  "Sidney", "Salt Laki City", "Athens", "Turin", "Beijing", "Vancouver", "London",
                  "Sochi", "Rio de Janeiro", "Pyeongchang", "Tokyo", "Beijing", "Paris", "Milan-Corina d'Ampezzo",
                  "Los Angeles"]

print(set(olympic_cities))
print(len(olympic_cities))
print(list(set(olympic_cities)))
print(len(list(set(olympic_cities))))

# set methods
scifi = {"star trek", "star wars", "halo"}
scifi.add("mass effect")
print(scifi)

fruits = {"apple", "orange", "banana", "tomato"}
fruits.remove("tomato")
print(fruits)
fruits.discard("pear")
print(fruits)
fruits.discard("apple")
print(fruits)

mountains = {"Everest", "Kilimanjaro", "Fuji"}
print(mountains)
mountains.clear()
print(mountains)

set_6 = mountains.copy()
print(set_6 is mountains)
print(set_6)

set_7 = {1, 2, 3, 4, 5}
set_8 = {6, 7, 8, 9, 10}
set_9 = set_7 | set_8
print(set_9)

set_10 = set_7.intersection(set_8)
print(set_10)

set_11 = set_8 - set_7
print(set_11)
set_11 = set_7.difference(set_8)

# set comprehensions
comp_1 = {even+2 for even in range(2, 11, 2)}
print(comp_1)

comp_2 = {char.lower() for char in "ALLCAPS"}
print(comp_2)
