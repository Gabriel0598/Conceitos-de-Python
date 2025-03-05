from collections.abc import Sequence
from typing import TypeAlias, NewType

def surface_area_of_cube(edge_length: float) -> str:
    return f"The surface area of cube is {6 * edge_length ** 2}."

print(surface_area_of_cube(5))

Vector = list[float]

def scale(scalar: float, vector: Vector) -> Vector:
    return [scalar * num for num in vector]

# passes type checking; a list of floats qualifies as a Vector.
new_vector = scale(2.0, [1.0, -4.2, 5.4])
print(new_vector)

type ConnectionOptions = dict[str, str]
type Address = tuple[str, int]
type Server = tuple[Address, ConnectionOptions]

def broadcast_message(message: str, servers: Sequence[Server]) -> None:
    ...

"""
The static type checker will treat the previous type signature as
being exactly equivalent to this one
"""
def broadcast_message(
        message: str
        , servers: Sequence[tuple[tuple[str, int], dict[str, str]]]
) -> None:
    ...

Vector: TypeAlias = list[float]

UserId = NewType('UserId', int)
some_id = UserId(524313)

def get_user_name(user_id: UserId) -> str:
    ...

# passes type checking
user_a = get_user_name(UserId(42351))
print(user_a)

# fails type checking; an int is not a UserId
user_b = get_user_name(-1)
print(user_b)

# 'output' is of type 'int', not 'UserId'
output = UserId(23413) + UserId(54341)
print(output)

UserId = NewType('UserId', int)
ProUserId = NewType('ProUserId', UserId)

def greeting(name: str) -> str:
    return 'Hello ' + name

print(greeting("Gabriel"))

def fun(m):
    for i in range(m):
        yield i # yield values one by one

# call the generator function
for num in fun(5):
    print(num)

def fun_multi(m):
    for i in range(m):
        yield i * i # yield values one by one

a = fun_multi(5)
for num in a:
    print(num)

def infinite_sequence():
    num = 0
    while True:
        yield num
        num += 1

gen = infinite_sequence()
for _ in range(10):
    print(next(gen), end=" ")

print("\n")
def fun_two(a):
    for num in a:
        if num % 2 == 0:
            yield num

a = [1, 4, 5, 6, 7]
print(list(fun_two(a)))

def fun(text, keyword):
    words = text.split()
    for word in words:
        if word == keyword:
            yield True

txt = "geeks for geeks"
search = fun(txt, "geeks")
print(sum(search))
