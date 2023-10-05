# Problem 1

try:
    # Open the file for reading
    with open('Python_Code/Module5_files/gettysburg.txt', 'r') as file:

        # Read the entire content of the files into a string
        file_contents = file.read()

    # Count the number of words
    words = file_contents.split()  # Split the content into words
    num_words = len(words)

    # Calculate the average length of words
    total_word_length = sum(len(word) for word in words)
    avg_word_length = total_word_length / num_words

    # Count the number of lines
    lines = file_contents.split('\n')  # Split the content into lines
    num_lines = len(lines)

    # Print the results
    print(f'Number of words: {num_words}')  # Print the number of words

    # Print the average lenght of words
    print(f'Average length of words: {avg_word_length:.2f} characters')

    print(f'Number of lines: {num_lines}')  # Print the Number of lines

except FileNotFoundError:
    # Handle the case where the file was not found
    print("The file 'Module5_files/gettysburg.txt' was not found.")

except IOError:
    # Handle any other IOError that might occur while reading the file
    print('An error occurred while reading the file "gettysburg.txt"')


# Print the Number of lines

# Problem 2


# Problem 3

# Problem 4

# Problem 5
