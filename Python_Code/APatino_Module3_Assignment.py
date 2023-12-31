# Problem 1

num_list = [13, 42, 10, 100, 30, 55, 111, 20, 23, 70, 95, 2]

# a. Used a while loop to look for the highest number in the list

# Initialized a variable to store the maximum value
max_num = num_list[0]  # Assumed that the first element is the highest value

# Initialized a variable for the loop counter
count = 1

# Started the loop from the second element in the list
while count < len(num_list):
    # Checked if the current element is greater than the current maximum number
    if num_list[count] > max_num:
        max_num = num_list[count]  # Updated the maximum value
    count += 1

# Print the maximum value found in the list
print("The highest number in the list is: ", max_num)

# b. Used a for loop to look for the lowest number in the list

# Initialize a variable to store the minimum value
min_num = num_list[0]

# Start the loop from the second element in the list (index 1)
for num in num_list:
    # Check if the current element is less than the current minimum
    if num < min_num:
        min_num = num  # Update the minimum value

# Print the lowest number found in the list
print("The lowest number in the list is: ", min_num)


# Problem 2

# Interactive adding machine

# General instructions
print(f"Initialized count by typying a valid number. The machine will continue to add each valid number that you type. If you desire to exit the adding machine type 'quit'.")

# Initialize the running total
added_num = 0

# Run until the user decides to quit
while True:

    num = input("Enter a number: ")

# Checks if the user wants to quit
    if num.lower() == "quit":
        print(f"The final addition was {added_num}.")
        break

# Checks if the input is a valid number
    try:
        # Convert the input to a floating-point number to accept floating points and negative numbers
        num = float(num)  # Accept float numbers without raising an Error
    except ValueError:
        print("Please enter a valid number or 'quit'.")
        continue  # Skip the rest of the loop and ask for input again

     # Add the number to the running total
    added_num += num
    print("Running total:", added_num)


# Problem 3

# Nested loop that finds as many unique pairs of integer numbers whose product is 120

# Initialized an empty list to store the pairs of integers
pairs = []

# Iterate through values of 'a' from 1 to 120
for a in range(1, 121):
    # Iterate through values of 'b' from 'a' to 120
    for b in range(1, 121):
        if a * b == 120 and a <= b:  # Checks that the product is 120 and a <= b to avoid permutations
            pairs.append((a, b))  # Append the pair (a, b) to the 'pairs' list

# Print the unique pairs
for pair in pairs:
    print(pair)


# Problem 4

# Floyd's Triangle

# User specifies the number of rows
num_rows = int(input("Enter the number of rows for Floyd's Triangle: "))

# Initialized variable that tracks the current number
current_num = 1

# Outer loop for rows, running from 1 to the specified number of rows
for row in range(1, num_rows + 1):
    # Inner loop for columns in each row, running from 1 to the current row number
    for column in range(1, row + 1):
        # end=" " controls the character that separates the printed items, a space is used to create the horizontal layout of numbers in the triangle.
        print(current_num, end=" ")
        current_num += 1
    # Move to the next line to start a new row
    print()


# Problem 5

# a. Filter out strings that contains numbers

current_list = ["Python", "1234", "4Sep23", "JavaScript", "2023", "React"]

# Initialized a list that stores the strings without numbers
filtered_list = []

# Iterate through the items in the current_list
for item in current_list:
    # Checks if there are any digits (numbers) present
    if not any(char.isdigit() for char in item):
        # If there are no digits it appends the item to the filtered_list
        filtered_list.append(item)

# Prints only the strings in the list
print(filtered_list)

# b. Comprehension version of 5a

filtered_list_v2 = [item for item in current_list if not any(
    char.isdigit() for char in item)]

print(filtered_list_v2)

# c.For loop that converts an arbitrary list of measurements in inches to meters

# Initialized list with a set of merasurements in inches
inches_list = [500, 330, 200, 600, 400, 999, 255, 39.37]

meters_list = []

# Iterate through the measurements in inches in the list of inches
for inch in inches_list:
    # Converts each measurement from inches to meters by divinding it by 39.37
    meter = inch / 39.37
    # Appends each value to a list of measurements in meters
    meters_list.append(meter)

# Prints the list which contains the measurements converted to meters
print(meters_list)

# d. Comprehension version of 5b

meters_list_v2 = [inch/39.37 for inch in inches_list]

print(meters_list_v2)
