# Problem 1

# Defined a function that takes the original dictionary as input and returns the reversed dictionary.
def reverse_dictionary(original_dict):
    reversed = {}  # Create an empty dictionary to store the reversed relationship

    for key, value in original_dict.items():  # Iterate through the original dictionary
        reversed[value] = key  # Swap the key and value

    return reversed  # Return the reversed dictionary


# Example usage:
original_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
reversed = reverse_dictionary(original_dict)
print(reversed)

# Problem 2

# Problem 3

# Problem 4

# Problem 5
