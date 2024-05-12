def decode(input_file):
    with open(input_file, 'r') as file:
        lines_fl = file.readlines()

    decoded_string = []
    for line in lines_fl:
        line = line.strip().split()
        decoded_string.append(line[-1])

    return ' '.join(decoded_string)


input_file = "C:/Users/Proprietario/Downloads/input_text.txt"
decoded_text = decode(input_file)
print(decoded_text)

# Original decoded text
# decoded_text = "love computers dogs cats I you"

# Split the decoded text into words
words = decoded_text.split()

# Extract the words starting from the index of "I" to the end
required_words = words[words.index("I"):]

# Join the required words into a single string
required_message = ' '.join(required_words)

print(required_message)
