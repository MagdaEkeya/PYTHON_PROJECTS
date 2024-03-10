# Sample list of words
word_list = ["apple", "banana", "orange", "grape", "kiwi", "peach", "pear", "plum"]

# Use list comprehension to create a new list with words having odd number of characters
odd_length_words = [word for word in word_list if len(word) % 2 != 0]

# Print the new list
print("Words with odd number of characters:", odd_length_words)
