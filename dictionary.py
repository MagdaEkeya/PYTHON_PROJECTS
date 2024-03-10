# Define an empty dictionary to store person's information
person_info = {}

# Ask user for input
name = input("Enter your name: ")
age = input("Enter your age: ")
favorite_color = input("Enter your favorite color: ")

# Store the information in the dictionary
person_info['name'] = name
person_info['age'] = age
person_info['favorite_color'] = favorite_color

# Print the dictionary to the console
print("Person's Information:")
for key, value in person_info.items():
    print(f"{key.capitalize()}: {value}")
