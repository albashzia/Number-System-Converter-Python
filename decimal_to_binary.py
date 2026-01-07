def decimal_to_binary(num):
    binary = ""
    number = num

    if number == 0:
        return "0"

    while number > 0:
        remainder = number % 2
        binary = str(remainder) + binary
        number = number // 2

    return binary

num = int(input("Enter a decimal number: "))
result = decimal_to_binary(num)
print("The number in binary is",result)
