from string import Template

print("Hello World")

a = 5
print("Type of a: ", type(a))

b = 5.0
print("\nType of b: ", type(b))

c = 2 + 4j
print("\nType of c: ", type(c))

String1 = 'Welcome to the Geeks World'
print("String with the use of Single Quotes: ")
print(String1)
String1 = "I'm a Geek"
print("\nString with the use of Double Quotes: ")
print(String1)
print(type(String1))
String1 = '''I'm a Geek and I live in a world of "Geeks"'''
print("\nString with the use of Triple Quotes: ")
print(String1)
print(type(String1))

String1 = '''Geeks 
            For 
            Life'''
print("\nCreating a multiline String: ")
print(String1)

String1 = "GeeksForGeeks"
print("Initial String: ")
print(String1)
print("\nFirst character of String is: ")
print(String1[0])
print("\nLast character of String is: ")
print(String1[-1])

List = []
print("\nInitial blank List: ")
print(List)
List = ['GeeksForGeeks']
print("\nList with the use of String: ")
print(List)
List = ["Geeks", "For", "Geeks"]
print("\nList containing multiple values: ")
print(List[0])
print(List[2])
List = [['Geeks', 'For'], ['Geeks']]
print("\nMulti-Dimensional List: ")
print(List)

List = ["Geeks", "For", "Geeks"]
print("\nAccessing element from the list")
print(List[0])
print(List[2])
print("\nAccessing element using negative indexing")
print(List[-1])
print(List[-3])

Tuple1 = ()
print("\nInitial empty Tuple: ")
print(Tuple1)
Tuple1 = ('Geeks', 'For')
print("\nTuple with the use of String: ")
print(Tuple1)
list1 = [1, 2, 4, 5, 6]
print("\nTuple using List: ")
print(tuple(list1))
Tuple1 = tuple('Geeks')
print("\nTuple with the use of function: ")
print(Tuple1)
Tuple1 = (0, 1, 2, 3)
Tuple2 = ('python', 'geek')
Tuple3 = (Tuple1, Tuple2)
print("\nTuple with nested tuples: ")
print(Tuple3)

tuple1 = tuple([1, 2, 3, 4, 5])
print("\nFirst element of tuple")
print(tuple1[0])
print("\nLast element of tuple")
print(tuple1[-1])

print("\nThird last element of tuple")
print(tuple1[-3])

set1 = set()
print("\nInitial blank Set: ")
print(set1)
set1 = set("GeeksForGeeks")
print("\nSet with the use of String: ")
print(set1)
set1 = set(["Geeks", "For", "Geeks"])
print("\nSet with the use of List: ")
print(set1)
set1 = set([1, 2, 'Geeks', 4, 'For', 6, 'Geeks'])
print("\nSet with the use of Mixed Values")
print(set1)

set1 = set(["Geeks", "For", "Geeks"])
print("\nInitial set")
print(set1)
print("\nElements of set: ")
for i in set1:
    print(i, end=" ")
print("Geeks" in set1)

Dict = {}
print("\nEmpty Dictionary: ")
print(Dict)
Dict = {1: 'Geeks', 2: 'For', 3: 'Geeks'}
print("\nDictionary with the use of Integer Keys: ")
print(Dict)
Dict = {'Name': 'Geeks', 1: [1, 2, 3, 4]}
print("\nDictionary with the use of Mixed Keys: ")
print(Dict)
Dict = dict({1: 'Geeks', 2: 'For', 3: 'Geeks'})
print("\nDictionary with the use of dict(): ")
print(Dict)
Dict = dict([(1, 'Geeks'), (2, 'For')])
print("\nDictionary with each item as a pair: ")
print(Dict)

Dict = {1: 'Geeks', 'name': 'For', 3: 'Geeks'}
print("\nAccessing a element using key:")
print(Dict['name'])
print("\nAccessing a element using get:")
print(Dict.get(3))

fruits = ["apple", "banana", "orange"]
print(fruits)
fruits.append("grape")
print(fruits)
fruits.remove("orange")
print(fruits)

coordinates = (3, 5)
print(coordinates)
print("\nX-coordinate:", coordinates[0])
print("Y-coordinate:", coordinates[1])

# String interpolation
n1 = 'Hello'
n2 = 'GeeksforGeeks'

# for single substitution
print("\nWelcome to % s" % n2)

# for single and multiple substitutions()
# mandatory
print("% s ! This is % s." % (n1, n2))

n1 = 'Hello'
n2 = 'GeeksforGeeks'

# for single substitution
print('\n{}, {}'.format(n1, n2))

n1 = "Hello"
n2 = "GeeksForGeeks"

# for single or multiple substitutions
# let's say b1 and b2 are formal parameters
# and n1 and n2 are actual parameters
print("\n{b1}! This is {b2}.".format(b1=n1, b2=n2))

# we can also change the order of the
# variables in the string without changing
# the parameters of format function
print("{b2}! This is {b1}.".format(b1=n1, b2=n2))

n1 = 'Hello'
n2 = 'GeeksforGeeks'

# f tells Python to restore the value of two
# string variable name and program inside braces {}
print(f"\n{n1}! This is {n2}")

a = 2
b = 3
c = 10

print(f"({a} * {b})-{c} = {(2 * 3)-10}")

n1 = 'Hello'
n2 = 'GeeksforGeeks'

# made a template which we used to
# pass two variable so n3 and n4
# formal and n1 and n2 actual
n = Template('$n3 ! This is $n4.')

# and pass the parameters into the template string.
print(n.substitute(n3=n1, n4=n2))
