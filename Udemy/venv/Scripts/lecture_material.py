print("Hello World")
ex_var = 5
# variable is changeable
ex_var = 7

#ex:
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
addition = 4 + 5 # 9
subtraction = 5 -2 # 3
division = 7 / 2 # 3.5
multiplication = 3 * 8 # 24

exponentiation = 4 ** 4 # 256
floor_division = 16 // 5 #
modulo = 7 % 3 # return the rest

add_assign = 5
add_assign += 7 # result = 12
# is like add_assign = add_assign + 7

# subtraction
sub = 10
sub -= 5 # 5
# multiplication
mult = 10
mult *= 5 # 50
# division
div = 10
div /= 5 # 2.0
# exponentiation
exp = 10
exp **= 2 # 100
# floor division
floor = 10
floor //= 6 # 1
# modulo
mod = 10
mod %= 7 # 3

# operator precedence = ()
# **
# % / // *
# + -

expression = (9-7) * 2 ** 3 + 10 % 6 // -1 * 2 - 1
print (expression)

example_1 = 3.14159
example_2 = 24601
example_3 = True
example_5 = 10 + 9

print(example_1)
print(example_2)
print(example_3)

print(example_5)
print((4 + 5) * 3)

var_ex = "Word" # variable definition of string
print(var_ex) # Print var_ex variable
print(2) # print number 2 directly
print(5 - 15 / 2) # print math operation

print(1.23 + 2.80)
ex2 = (123 + 280) / 10
print(ex2) # approximation
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
ex_7 = "0123456" # index begins with 0
ex_8 = "orange"
print(ex_8[2])
print("apple"[4])

ex_10 = "apricots"
print(ex_10[:3]) # show all positions before 3 less the 3 in end, so: 0 1 2 (apr)
print(ex_10[2:5]) # show all positions between 2 and 5, less the 5 in end, so 2 3 4 5 (ric)
print(ex_10[4:]) # show all positions after 4, incluind 4, so: 4 5 6 7 (cots)
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
ex_4 = str(True) # convert for string
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
print("This\tis\ta\tlot\tof\tspace.") # Tab
print("line one\nline two") # break line
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
    print (num1 * num2)
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
example_4 = "Hello World" # global

def loc_ex():
    example_4 = "This is a string" # local
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
    return # loc()

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
print("Hello" == "hello") # Case sensitive
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