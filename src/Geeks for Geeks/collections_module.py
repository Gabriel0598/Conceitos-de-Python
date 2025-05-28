from collections import ChainMap, Counter

# Collections
# https://www.geeksforgeeks.org/python-collections-module/

# Python program to demonstrate
# ChainMap
d1 = {'a':1, 'b':2}
d2 = {'c':3, 'd':4}
d3 = {'e':5, 'f':6}

# Defining the chainmap
c = ChainMap(d1, d2, d3)
print(c)

#-------------------------------------------
# A Python program to show different
# ways to create Counter
# With sequence of items
print(Counter(['B','B','A','B','C','A','B','B','A','C']))

# With dictionary
print(Counter({'A':3, 'B':5, 'C':2}))

# With keyword arguments
print(Counter(A=3, B=5, C=2))