def large_power(base, exponent):
    # Calculate the result of base raised to the exponent
    result = base ** exponent
    
    # Check if the result is greater than 5000
    if result > 5000:
        return True
    else:
        return False

# Example usage:
print(large_power(10, 3))  # Output will be False
print(large_power(10, 4))  # Output will be True
