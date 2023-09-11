import string

# Problem 1

# Defined a function that takes the original dictionary as input and returns the reversed dictionary.


def reverse_dictionary(original_dict):
    reversed_dict = {}  # Create an empty dictionary to store the reversed relationship

    for key, value in original_dict.items():  # Iterate through the original dictionary
        reversed_dict[value] = key  # Swap the key and value

    return reversed_dict  # Return the reversed dictionary


# Example usage:
original_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
reversed_dict = reverse_dictionary(original_dict)
print(reversed_dict)


# Problem 2

# Function counts the words in the input sentence and return a dictionary with word counts
def str_to_word_count(sentence):
    sentence = sentence.lower()  # Preprocess the input by converting it to lowercase

    words = sentence.split()  # Split the sentence into words

    word_count = {}  # Count the words

    for word in words:

        # Use strip() to remove leading and trailing punctuation
        word = word.strip(string.punctuation)

        # Check if the word is not empty after stripping punctuation
        if word:
            # Check if the word is already in the dictionary, and update its count
            # or initialize it with a count of 1 if it's not in the dictionary
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1

    return word_count  # Return the dictionary with word counts


sentence = input("Write a sentence: ")
result = str_to_word_count(sentence)
print(result)

# Problem 3

# Problem 4

# Problem 5
