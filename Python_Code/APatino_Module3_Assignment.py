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

added_num = 0

# Run until the user decides to quit
while True:

    num = input("Enter the first number: ")

# Checks if the user wants to quit
    if num.lower() == "quit":
        print(f"The final addition was {added_num}.")
        break

# Checks if the input is a valid number
    try:
        # Convert the input to a floating-point number to accept floating points and negative numbers
        num = float(num)
    except ValueError:
        print("Please enter a valid number or 'quit'.")
        continue  # Skip the rest of the loop and ask for input again

     # Add the number to the running total
    added_num += num

    print(f"The final addition was ", {added_num})

# Problem 3

# Problem 4

# Problem 5

# a.

# b.

# c.

# d.
