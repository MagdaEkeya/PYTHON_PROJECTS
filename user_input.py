# User input for the first set of integers
input_set1 = input("Enter elements for the first set (separated by spaces): ")
set1 = set(map(int, input_set1.split()))

# User input for the second set of integers
input_set2 = input("Enter elements for the second set (separated by spaces): ")
set2 = set(map(int, input_set2.split()))

# Find the common elements between the two sets
common_elements = set1.intersection(set2)

# Print the common elements
print("Common elements in both sets:", common_elements)
