def letters_to_ascii(input_string):
        ascii_values = []
        for char in input_string:
            ascii_value = ord(char)
            ascii_values.append(ascii_value)
        return ascii_values

def convert(inputText):
    try:
        ascii_output = letters_to_ascii(inputText)
        print(f"ASCII коды: {ascii_output}")
    except ValueError as e:
        print(e)

input_string = input("Input text: ")
convert(input_string)