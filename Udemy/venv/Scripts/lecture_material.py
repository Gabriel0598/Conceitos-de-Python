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

