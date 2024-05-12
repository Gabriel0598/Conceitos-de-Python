# Concatening exercise
import switcher as switcher

var_1 = 3.14159
print(type(var_1))
print(str(var_1) + " is a float.")
name = "Gabriel"
print("Hello, i'm " + name + " it's nice to meet you!")

print("*******\n ***** \n  ***  \n   *   ")

# Just do it exercice
just = "Just do it!"
print(just[10:])
print(just[5:7])
print(just[8:10])
print(just[0:4])
print("Don't " + just[5:11])
'''
# Input exercise
name = input("What is your name? ")
quest = input("What is your quest? ")
color = input("What is your favorite color? ")

print("So your name is " + name + ", your quest is " + quest + ", and your favorite color is " + color + ".")

int_1 = int(input("Enter with a number: "))
print(int_1 + 10)
'''


def hello_world_printer():
    print("Hello World")


hello_world_printer()

name


def name_printer(user_name):
    print(user_name)


'''
name = input("Please enter your name: ")
name_printer(name)

length = int(input("Enter an integer that represents length in feet: "))
width = int(input("Enter an integer that represents width in feet: "))
height = int(input("Enter an integer that represents height in feet: "))

def prism_vol(l, w, h):
    return l * w * h

print("The volume of the rectangular prism is " + str(prism_vol(length, width, height)) + " cubic feet.")
###

###
celsius = int(input("Enter an temperature in celsius degree: "))
def fahrenheit(cel):
    return round((1.8 * cel + 32), 1)

print("The Fahrenheit equivalent of " + str(celsius) + " degrees Celsius is " + str(fahrenheit(celsius)) + ".")
'''
from random import randint

gallons = (randint(10, 25))
miles = (randint(200, 400))

# formula = miles per gallon (MPG) = miles driven/gallons used
MPG = miles // gallons
print("The car can travel " + str(MPG) + " Miles per gallon.")
print("The car's fuel tank can hold " + str(gallons) + " gallons.")
print("The car can travel " + str(miles) + " miles on a full tank.")
"""
# Grade determine
score = int(input("Please enter the student's score: "))

if score >= 90:
    print("This student's score of " + str(score) + " is an A.")
else:
    if score >= 80:
        print("This student's score of " + str(score) + " is a B.")
    else:
        if score >= 70:
            print("This student's score of " + str(score) + " is a C.")
        else:
            if score >= 60:
                print("This student's score of " + str(score) + " is a D.")
            else:
                print("This student's score of " + str(score) + " is a F.")
"""
# Roman numeral equivalent
import random

# call two integers between 1 and 10:
rand_num = (random.randint(1, 10))
print("Random number: " + str(rand_num))

if rand_num == 1:
    print("I")
elif rand_num == 2:
    print("II")
elif rand_num == 3:
    print("III")
elif rand_num == 4:
    print("IV")
elif rand_num == 5:
    print("V")
elif rand_num == 6:
    print("VI")
elif rand_num == 7:
    print("VII")
elif rand_num == 8:
    print("VIII")
elif rand_num == 9:
    print("IX")
else:
    print("X")

"""
# Function containing dictionary
import random

# call two integers between 1 and 10:
rand_num2 = (random.randint(1, 10))
print("Random number: " + str(rand_num2))

def switch_roman_num(num):
    switcher == rand_num2
    {
        # Equivalent roman number:
        1: "I",
        2: "II",
        3: "III",
        4: "IV",
        5: "V",
        6: "VI",
        7: "VII",
        8: "VIII",
        9: "IX",
        10: "X"
    }
print(switch_roman_num(switcher))
"""

# While loops
counter = 10
while counter >= 1:
    print(counter)
    counter -= 1
"""
# Sum of numbers
counter # Used to increase the integer
pos_int = int(input("Type a integer: "))
int_init = pos_int
summed = 0
while pos_int > 0:
    summed += pos_int
print(int_init)
print(summed)
"""
# Loop
word= "Hello World"
for letter in word:
    print(letter)
"""
# String solution
user_str = input("Please enter a string: ")
count = 0

for char in user_str:
    count += 1

print(user_str)
print(count)
"""
# Fizz Buzz
for num in range(1, 51):
    if num%3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)

# Factorial
def factorial(fac_num):
    returned = 1
    for item in range(fac_num, 1, -1):
        returned *= item
    return returned

print(factorial(3)) # 6
print(factorial(4)) # 24
print(factorial(5)) # 120

# String methods
mixed_case = "A Song of Ice and Fire"
print(mixed_case.isupper())
print(mixed_case.islower())
print(mixed_case.upper())
print(mixed_case.lower())
print(mixed_case.istitle())
title_case = mixed_case.title()
print(title_case)
print(mixed_case.startswith("A"))
print(mixed_case.endswith("e"))
words = mixed_case.split()
print(words)
print("".join(words).isalpha())

the_string = "North Dakota"
print(the_string.rjust(17))
print(the_string.ljust(17, "*"))
center_plus = the_string.center(16, "+")
print(center_plus)
print(the_string.lstrip("North"))
print(center_plus.rstrip("+"))
print(center_plus.strip("+"))
print(the_string.replace("North", "South"))
"""
# String reverser
user_string = input("Please enter a string: ")
reversed = ""

for item in range(len(user_string) -1, -1, -1):
    reversed += user_string[item]

print(reversed)
"""

# Word counter
str_1 = "Anyway, like I was sayin', shrimp is the fruit of the sea. You can barbecue it, boil it, broil it, bake it, \
saute it. Dey's uh, shrimp-kabobs, shrimp creole, shrimp gumbo. Pan fried, deep fried, stir-fried. There's pineapple \
shrimp, lemon shrimp, coconut shrimp, pepper shrimp, shrimp soup, shrimp stew, shrimp salad, shrimp and potatoes, \
shrimp burger, shrimp sandwich. That- that's about it."

spaces_and_letters = ""

# this for loop reduces the string to letters, numbers, and spaces
for char in str_1:
    if char.isalnum() or char.isspace() or char == "-" or char == "'":
        spaces_and_letters += char

# .split() is used to put the words the into a list
words = spaces_and_letters.split()
number_of_words = len(words)

print(words)
print(number_of_words)

# List exercises
ex_list_1 = [1,3.14159,True,"text",[3,9,7]]
print(ex_list_1)
call_list = ex_list_1
verify_list = "e" in call_list
verify_list2 = "a" not in call_list
print(verify_list, verify_list2)

# indexes and list slicing
up_by_two = [[0,2],[4,6],[8,10],[12,14]]
print(up_by_two[0])
print(up_by_two[3][1])
furniture = ["chair", "table", "desk", "lamp", "bed"]
print(furniture[-5])
print("Most people own at least " + str(up_by_two[0][1]) + "" + furniture[0] + "s.")
floats = [0.98, 8.76, 6.54, 4.32]
print(floats[1:])
print(floats[1:3])
print(floats[:2])

# del and list
arctic_animals = ["penguin", "elephant", "polar bear", "walrus", "tiger", "reindeer"]
del arctic_animals[4]
arctic_animals.remove("elephant")
arctic_animals.append("arctic fox")
arctic_animals.insert(2, "snowy owl")
arctic_animals.sort()
print(arctic_animals)
print(arctic_animals.index("reindeer"))
print(arctic_animals.pop())

# dictionaries
dictionary = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}
print(dictionary["c"])
print("a" in dictionary)
print("b" not in dictionary)

# dictionary
famous_songs = {"Queen": "Bohemian Rhapsody",
                "Bee Gees": "Stayin' Alive",
                "U2": "One",
                "Michael Jackson": "Billie Jean",
                "The Beatles": "Hey Jude",
                "Bob Dylan": "Like a Rolling Stone"}
print(len(famous_songs))
for key in famous_songs.keys():
    print(key)
print(famous_songs.values())
for key, value in famous_songs.items():
    print(key, value)
print(famous_songs.get("Promise of the Real", "That is not a key that appears in the dictionary."))

# Dictionary methods
for key, value in {}.fromkeys("bcdfghjklmnpqrstvwxyz", "consonant").items():
    print(key, value)

fast_food_items = {"McDonald's": "Big Mac", "Burger King": "Whopper", "Chick-fil-A": "Original Chicken Sandwich"}
print(fast_food_items.pop("McDonald's"))

fast_food_items.popitem()
print(fast_food_items)

# Dictionary methods
internet_celebrities = {"DrDisrespect": "YouTube", "Zlaner": "Facebook", "Ninja": "Mixer"}
another_one = {"shroud": "Twitch"}
internet_celebrities.update(another_one)
gamers = internet_celebrities.copy()
internet_celebrities.clear()
print(internet_celebrities)
print(gamers)

# Switch case
lang = input("What's the programming language you want to learn? ")

match lang:
    case "JavaScript":
        print("You can become a web developer.")

    case "Python":
        print("You can become a Data Scientist")

    case "PHP":
        print("You can become a backend developer")

    case "Solidity":
        print("You can become a Blockchain developer")

    case "Java":
        print("You can become a mobile app developer")
    case _:
        print("The language doesn't matter, what matters is solving problems.")