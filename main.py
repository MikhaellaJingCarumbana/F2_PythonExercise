# Custom implementation of decimal to binary conversion
def decToBinary(dec):
    if dec == 0:
        return "0b0"

    binary = ""
    while dec > 0:
        remainder = dec % 2
        binary = str(remainder) + binary
        dec = dec // 2

    return "0b" + binary

# Custom implementation of binary to decimal conversion
def binaryToDecimal(bin_str):
    decimal = 0
    base = 1
    bin_str = bin_str.lstrip('0b')

    for digit in bin_str[::-1]:
        decimal += int(digit) * base
        base *= 2

    return decimal

# Custom implementation of decimal to octal conversion
def decToOctal(dec):
    if dec == 0:
        return "0o0"

    octal = ""
    while dec > 0:
        remainder = dec % 8
        octal = str(remainder) + octal
        dec = dec // 8

    return "0o" + octal

# Custom implementation of decimal to hexadecimal conversion
def decToHex(dec):
    if dec == 0:
        return "0x0"

    hex_chars = "0123456789ABCDEF"
    hex_str = ""
    while dec > 0:
        remainder = dec % 16
        hex_str = hex_chars[remainder] + hex_str
        dec = dec // 16

    return "0x" + hex_str

# Main function to call all the custom functions
def main():
    decimal = 0
    is_valid_decimal = False
    while not is_valid_decimal:
        decimal_input = input("Enter a decimal number: ")
        if decimal_input.isdigit():
            decimal = int(decimal_input)
            is_valid_decimal = True
        else:
            print("Invalid input. Please enter a valid decimal number.")

    print("Decimal:", decimal)

    binary = decToBinary(decimal)
    print("Binary:", binary)

    octal = decToOctal(decimal)
    print("Octal:", octal)

    hexadecimal = decToHex(decimal)
    print("Hexadecimal:", hexadecimal)

    is_valid_binary = False
    while not is_valid_binary:
        binary_repr = input("Enter a binary representation (e.g., 0b101010): ")
        binary_str = binary_repr[2:] if binary_repr.startswith("0b") else binary_repr
        if all(bit in "01" for bit in binary_str):
            is_valid_binary = True
        else:
            print("Invalid binary input. Please enter a valid binary representation.")

    base = 0
    while base not in (2, 8, 16):
        base_input = input("Enter the target base (2, 8, or 16): ")
        if base_input.isdigit():
            base = int(base_input)
        else:
            print("Invalid base input. Please enter a valid base.")

    if base == 2:
        result = binary_repr
    elif base == 8:
        result = decToOctal(binaryToDecimal(binary_repr))
    elif base == 16:
        result = decToHex(binaryToDecimal(binary_repr))

    print(f"Convert {binary_repr} to base {base}:", result)

if __name__ == "__main__":
    main()
