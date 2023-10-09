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

# Handle Exceptions
except FileNotFoundError:
    # Handle the case where the file was not found
    print("The file 'gettysburg.txt' was not found.")

except IOError:
    # Handle any other IOError that might occur while reading the file
    print('An error occurred while reading the file "gettysburg.txt"')


# Problem 2

# Create a new file containing only 5 letter words

try:
    # Open the file for reading
    with open('Python_Code/Module5_files/words.txt', 'r') as input_file:

        # Create a new output file for writing
        with open('Python_Code/Module5_files/5letter_words.txt', 'w') as output_file:

            # Initialize counters
            original_num_words = 0
            new_num_words = 0

            # Iterate through each line in the input file
            for line in input_file:
                # Split the line into words
                words = line.split()

                # Iterate through each word in the line
                for word in words:
                    # Remove newlines and calculate word length
                    word = word.strip()
                    word_length = len(word)

                    # Check if the word has exactly 5 characters
                    if word_length == 5:
                        # Write the word to the new file
                        output_file.write(word + '\n')
                        new_num_words += 1

                    # Increment the original file word count
                    original_num_words += 1

    # Print the number of words in the original file
    print(
        f'The number of words in the original file: {original_num_words}')

    # Print the number of words in the new file
    print(f'The number of words in the new file: {new_num_words}')


# Handle Exceptions
except FileNotFoundError:
    # Handle the case where the file was not found
    print("The file 'words.txt' was not found.")

except IOError:
    # Handle any other IOError that might occur while reading the file
    print('An error occurred while reading/ writing the file 5letter_words.txt')

# Problem 3

# Problem 4

# Problem 5
