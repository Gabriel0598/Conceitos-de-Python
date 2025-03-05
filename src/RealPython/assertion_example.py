# Assertion introduce
# May success
number = 42
assert number > 0, f"Number greater than 0 expected, got: {number}"

# May fail/ AssetionError
number = -42
assert number > 0, f"Number greater than 0 expected, got: {number}"

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