import re

def decode(message_file):
    """
    :param message_file:
    Decodes a message from a text file containing words and numbers
    in a pyramid structure.
    Args:
    message_file: The path to the text file containing the encoded message.
    :return:
    The decoded message as a string.
    """

    with (open(message_file, "r") as file):
        lines = file.readlines()

        # Build the pyramid structure
        pyramid = []

        for line in lines:
            line = line.strip()
            if not line:
                continue
            try:
                number, word = line.split(" ")
                pyramid.append((int(number), word))
            except ValueError:
                print(f"Warning: Invalid format in line '[line]'")
                continue

        # Extract words corresponding to numbers 1, 3, and 6
        message_words = [row[1] for row in pyramid if row[0] in (1, 3, 6)]

        # Ensure the words are in the correct order
        message_words.sort(key=lambda x: pyramid.index((1, x)) if (1, x) in pyramid else float('inf'))

        return " ".join(message_words)

# Extracting from a file
input_file = "C:/Users/Proprietario/Downloads/input_text.txt"
message_file = input_file
decoded_message = decode(message_file)
print("Decoded message: ", decoded_message)
