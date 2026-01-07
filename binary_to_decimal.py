def binary_to_decimal(string):
    decimal_number = 0

    for digit in string:
        decimal_number = decimal_number * 2 + int(digit)

    return decimal_number

string = input("Enter a binary number: ")
result = binary_to_decimal(string)
print("The number in decimal is",result)
