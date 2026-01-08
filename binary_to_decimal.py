# function to take a binary string and return a decimal number of it
def binary_to_decimal(string):
    decimal_number = 0 # initializing the string
    # looping over the whole input string
    for digit in string:
        decimal_number = decimal_number * 2 + int(digit)
    # returning the decimal number
    return decimal_number

# main program
string = input("Enter a binary number: ") # taking input from the user
result = binary_to_decimal(string) # call to function 
print("The number in decimal is",result) # print the result 
