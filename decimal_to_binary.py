# function to convert a decimal number to binary
def decimal_to_binary(num):
    binary = "" # initializing an empty string to hold results
    number = num # assigning input number to number
    
    # dealing if the number entered is 0
    if number == 0:
        return "0"

    # looping over the number until the number is greater than 0 
    while number > 0:
        remainder = number % 2 
        binary = str(remainder) + binary
        number = number // 2
    # returning the result string 
    return binary
    
# main program
num = int(input("Enter a decimal number: ")) # taking input from the user
result = decimal_to_binary(num) # call to function  
print("The number in binary is",result) # printing the results to console
