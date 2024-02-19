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
        current_row = []

        # print(pyramid)
        # print(lines)
        for line in lines:
            line = line.strip()
            if not line:
                continue
            try:
                number, word = line.split(" ")
                # .strip()
                # number = int(number)
                # current_row.append((number, word))
                pyramid.append((int(number), word))
                # print(pyramid)
                # print(lines)
                # print(line)
            except ValueError:
                print(f"Warning: Invalid format in line '[line]'")
                continue

        # Extract words corresponding to numbers 1, 3, and 6
        message_words = [row[1] for row in pyramid if row[0] in (1, 3, 6)]

        # Ensure the words are in the correct order
        message_words.sort(key=lambda x: pyramid.index((1, x)) if (1, x) in pyramid else float('inf'))

        return " ".join(message_words)

        # message = " ".join(row[1] for row in pyramid if row[0] in (1, 3, 6))
        # for row in pyramid:
        #     if len(row) >= 2:
        #         """message += row[-1][1]  # Access word directly"""
        #         # if row[-1][1] == "I":
        #         #     message += "I "
        #         # elif row[-1][1] == "love":
        #         #     message += "love "
        #         # elif row[-1][1] == "computers":
        #         #     message += "computers"
        #         message += row[1] + " "
        #     else:
        #         print("Warning: Empty or invalid row")


        # return message
        # .strip()


            # Check if this line contains "I" and add it to message
            # if "I" in word:
            #     message += word + " "

            # match word:
            #     case "I":
            #         message += word + " "
            #     case "love":
            #         message += word + " "
            #     case "computers":
            #         message += word + " "



            # print(lines)
            # print(line)

            # print(current_row)
            # print(pyramid)
            # if len(current_row) == len(pyramid) + 1:
            #     pyramid.append(current_row)
            #     current_row = []
                # print(current_row)
                # print(pyramid)

    # return message

        # print(type(pyramid))
        # print(type(current_row))
        # print(pyramid)
        # print("")
        # print(current_row)

        # Extract the message from the end of each pyramid row
        # message = "I "
        # for row in pyramid:
        #     message += row[-1][1]
        #
        # return message

        # Extract the exact message required:
        # message
        # for line in pyramid:
        #     if line == (line.find(1)):
        #         print("1 Encontrado")
        #         print(line)

            # first_word = re.search("I", line)

# Example usage
input_file = "C:/Users/Proprietario/Downloads/input_text.txt"
message_file = input_file
decoded_message = decode(message_file)
print("Decoded message: ", decoded_message)
