# Initializing string
import base64
String = "geeksforgeeks"

encoded_string = String.encode('utf-8')
print('The encoded string in base64 format is: {}'.format(encoded_string))
# print(encoded_string)

decoded_string = encoded_string.decode('utf-8')
print('The decoded string is: {}'.format(decoded_string))
# print(decoded_string)

## second example
user = "geeksforgeeks"
pswd = "i_lv_coding"

# Converting password to base 64 encoding
pswd_encoded = base64.b64encode(pswd.encode('utf-8')).decode('utf-8')
user_login = "geeksforgeeks"

# Wrongly entered password
pswd_wrong = "geeksforgeeks"
print("Password entered: ", pswd_wrong)

if pswd_wrong == base64.b64decode(pswd_encoded).decode('utf-8'):
    print("You are loggen in!")
else:
    print("Wrong password!")

print()

# Correctly entered password
pswd_right = "i_lv_coding"
print("Password entered: ", pswd_right)

if pswd_right == base64.b64decode(pswd_encoded).decode('utf-8'):
    print("You are logged in!")
else:
    print("Wrong password!")
