# function to validate if input is in decimal format
def validate_decimal_input(input_str):
    try:
        # try converting input to decimal
        decimal_value = int(input_str)
        return True, decimal_value
    except ValueError:
        # if conversion fails, input is not in decimal format
        return False, None

# function to convert decimal to hexadecimal
def decimal_to_hexadecimal(decimal_value):
    # Initialize variables
    hexadecimal_digits = "0123456789ABCDEF"
    hexadecimal_result = ""

    # loop to convert decimal to hexadecimal
    while decimal_value > 0:
        remainder = decimal_value % 16
        hexadecimal_result = hexadecimal_digits[remainder] + hexadecimal_result
        decimal_value = decimal_value // 16

    return hexadecimal_result

# function to validate if input is in hexadecimal format
def validate_hexadecimal_input(input_str):
    # Define valid hexadecimal characters
    valid_hex_chars = set("0123456789ABCDEF")

    # check if all characters in input are valid hexadecimal characters
    if all(char in valid_hex_chars for char in input_str):
        return True
    else:
        return False

# function to convert hexadecimal to decimal
def hexadecimal_to_decimal(hexadecimal_str):
    # Initialize variables
    decimal_value = 0

    # iterate through each hexadecimal digit in reverse order
    for i, char in enumerate(reversed(hexadecimal_str)):
        # Calculate decimal value of each digit and add to total
        decimal_value += int(char, 16) * (16 ** i)

    return decimal_value

# main program
if __name__ == "__main__":
    # Part a: Decimal to Hexadecimal conversion
    decimal_input = input("Enter a decimal number: ")

    # validate decimal input
    is_decimal, decimal_value = validate_decimal_input(decimal_input)

    if is_decimal:
        # convert decimal to hexadecimal
        hexadecimal_result = decimal_to_hexadecimal(decimal_value)
        print("Hexadecimal equivalent:", hexadecimal_result)
    else:
        print("Invalid input. Please enter a valid decimal number.")

    #  Hexadecimal to Decimal conversion
    hexadecimal_input = input("Enter a hexadecimal number: ")

    # validate hexadecimal input
    is_hexadecimal = validate_hexadecimal_input(hexadecimal_input)

    if is_hexadecimal:
        # convert hexadecimal to decimal
        decimal_result = hexadecimal_to_decimal(hexadecimal_input)
        print("Decimal equivalent:", decimal_result)
    else:
        print("Invalid input. Please enter a valid hexadecimal number.")
