# Concatening exercise
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

# Grade determine
score = int(input("Please enter the student's score. "))

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

