# Ask the user for a list of numbers
user_input = input("Enter a list of integers separated by spaces and press Enter: ")

# Convert the string of numbers into a list of integers
int_list = [int(x) for x in user_input.split()]

# Compute the sum of the integers
total_sum = sum(int_list)

# Print the sum 
print("The sum of the integers is:", total_sum)
