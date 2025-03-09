# Assertion introduce
# May success
number = 42
assert number > 0, f"Number greater than 0 expected, got: {number}"

# May fail/ AssetionError
# number = -42
# assert number > 0, f"Number greater than 0 expected, got: {number}"

# Syntax warning
number = 42
"""
assert (number > 0, f"Number greater than 0 expected, got: {number}")
"""

# Incorrect parenthesis use
"""
number = 42
assert (
    number > 0 and isinstance(number, int),
    f"Number greater than 0 expected, got: {number}"
)
"""

# Correct multiline
number = 42
assert number > 0 and isinstance(number, int), \
    f"Number greater than 0 expected, got: {number}"

# Assertion in parenthesis
number = 42
assert (number > 0)

# number = -42
# assert (number > 0)

# Comparison assertions
assert 3 > 2
# assert 3 == 2

assert 3 > 2 and 5 < 10
# assert 3 == 2 or 5 > 10

# Membership assertion
numbers = [1, 2, 3, 4, 5]
assert 4 in numbers
# assert 10 in  numbers

# Identity assetions
x = 1
y = x
null = None

assert x is y
# assert x is not y

# Type check assertions
number = 42
assert isinstance(number, int)

number = 42.0
# assert isinstance(number, int)

# All may be true
assert all([True, True, True])
# assert all([True, False, True])

# Any of them may be true
assert any([False, True, False])
# assert any([False, False, False])

# Functions for assertion test
def test_sum():
    assert sum([1, 2, 3]) == 6

def test_len():
    assert len([1, 2, 3]) > 0

def test_reversed():
    assert list(reversed([1, 2, 3])) == [3, 2, 1]

def test_membership():
    assert 3 in [1, 2, 3]

def test_isinstance():
    assert isinstance([1, 2, 3], list)

def test_all():
    assert all([True, True, True])

def test_any():
    assert any([False, True, False])

def test_always_fail():
    # assert pow(10, 2) == 42
    "Assert"

# Invoke functions
test_sum()
test_len()
test_reversed()
test_membership()
test_isinstance()
test_all()
test_any()
test_always_fail()