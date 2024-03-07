def indian_currency(num):
    # Convert the integer input to a string
    num_str = str(num)
    
    # Get the length of the string
    length = len(num_str)
    
    # If the length is less than or equal to 3, return the string as it is
    if length <= 3:
        return num_str
    # If the length is less than or equal to 5, insert a comma after the first group of digits
    elif length <= 5:
        return num_str[:-3] + "," + num_str[-3:]
    # For lengths greater than 5, insert commas after every two groups of digits
    else:
        return num_str[:-5] + "," + num_str[-5:-3] + "," + num_str[-3:]

# Example usage:
num = 504678
print(indian_currency(num))