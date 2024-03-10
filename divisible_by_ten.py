def divisible_by_ten(num):
    # Calculate the remainder of the input divided by 10
    remainder = num % 10
    
    # Check if the remainder is 0
    if remainder == 0:
        return True
    else:
        return False

# Example usage:
print(divisible_by_ten(20))  # Output will be True
print(divisible_by_ten(25))  # Output will be False
