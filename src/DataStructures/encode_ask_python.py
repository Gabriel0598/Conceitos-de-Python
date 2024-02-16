inp_string = "Hello"
bytes_encoded = inp_string.encode()
print(type(bytes_encoded))

a = 'This is a simple sentence'
print("Original string: ", a)

# Decodes to utf-8 by default
a_utf = a.encode()

print('Encoded string: ', a_utf)

a = 'This is a bit möre cömplex sentence.'

print('Original string: ', a)

print('Encoding with errors=ignore: ', a.encode(encoding='ascii', errors='ignore'))
print('Encoding with errors=replace: ', a.encode(encoding='ascii', errors='replace'))
# print('Encoding with errors=backslas: ', a.encode(encoding='ascii', errors='backslas'))
# print('Encoding with errors=hreplace: ', a.encode(encoding='ascii', errors='hreplace'))
# print('Encoding with errors=strict: ', a.encode(encoding='ascii', errors='strict'))

input_string = "abc123"
encoded = input_string.encode()
# Using decode()
decoded = encoded.decode()
print(encoded)
print(decoded)

bytes_seq = b'Hello'
decoded_string = bytes_seq.decode()
print(type(decoded_string))
print(decoded_string)

a = "This is a bit möre cömplex sentence."

print('Original string: ', a)

# Encoding in UTF-8
encoded_bytes = a.encode('utf-8', 'replace')

# Trying to decode via ASCII, which is incorrect
decoded_incorrect = encoded_bytes.decode('ascii', 'replace')
decoded_correct = encoded_bytes.decode('utf-8', 'replace')

print("Incorrectly decoded string: ", decoded_incorrect)
print("Correctly decoded string: ", decoded_correct)
