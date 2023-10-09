import json
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

import csv

# Read the CSV Data
data = []
with open('Python_Code/Module5_files/sf_buildings.csv', 'r') as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        data.append(row)

# Remove the 'use' column
for row in data:
    del row['use']

# Convert the height from feet to meters
for row in data:
    row['height'] = float(row['height']) * 0.3048
# Write the new data to a new CSV file
field_names = data[0].keys()

with open('Python_Code/Module5_files/sf_buildings_conversion.csv', 'w', newline='') as new_csv_file:
    writer = csv.DictWriter(new_csv_file, fieldnames=field_names)

    writer.writeheader()
    for row in data:
        writer.writerow(row)

# Problem 4

# Read the JSON data
try:
    with open('Python_Code/Module5_files/us_states_and_cities.json', 'r') as json_file:
        data = json.load(json_file)
except FileNotFoundError:
    print("Error: The JSON file 'us_states_and_cities.json' was not found.")
except json.JSONDecodeError:
    print("Error: There was an issue decoding the JSON data.")
else:

    # Find the state with the most cities
    max_state = ''
    max_city_count = 0

    for state, cities in data.items():
        city_count = len(cities)
        if city_count > max_city_count:
            max_city_count = city_count
            max_state = state
    # Print the name of the state with the most cities and number of cities it has
    print(
        f'The state with the most cities is {max_state} with {max_city_count} cities.')

    # Find the most common city name
    city_counts = {}

    for cities in data.values():
        for city in cities:
            city_counts[city] = city_counts.get(city, 0) + 1

    most_common_city = max(city_counts, key=city_counts.get)
    num_states_with_most_common_city = city_counts[most_common_city]

    # Print the most common city name across the states and the number of states that have that city name
    print(f'The most common city name is {most_common_city}')
    print(f'It appears in {num_states_with_most_common_city} states.')
