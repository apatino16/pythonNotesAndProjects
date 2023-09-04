## While Loop:

- A while loop is used when you want to repeatedly execute a block of code as long as a specified condition is true.
- It's important to initialize any variables used in the condition before the loop starts.
- You must include code within the loop that eventually changes the condition so that the loop will terminate; otherwise, you may end up with an infinite loop.
- A while loop can be useful when you don't know in advance how many iterations you'll need.

The syntax of a while loop in Python is as follows:

```
while condition:
    # Code to be executed as long as the condition is True
    # This code block is indented and continues until the condition becomes False
    # You can have multiple statements inside the loop

```

components Breakdown:

- `while`: This keyword is used to start a while loop.
- `condition`: This is the condition that is evaluated before each iteration of the loop. If the condition is True, the loop continues to execute; if it becomes False, the loop terminates.
- `:` (colon): It signifies the start of a new block of code, and all statements inside the loop must be indented to the same level.

Example of a while loop in Python that prints the highest number from a list:

```
num_list = [13, 42, 10, 100, 30, 55, 111, 20, 23, 70, 95, 2]

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

```

### For Loop:

- A for loop is used when you want to iterate over a sequence (such as a list, tuple, string, or range) and perform a certain action for each element in the sequence.
- You don't need to explicitly manage a loop counter variable; the for loop handles it for you.
- For loops are typically used when you know in advance how many iterations you need, or when you want to iterate over the elements of a collection.
- For loops are often more concise and easier to read than equivalent while loops for iterating over sequences.

The syntax of a for loop in Python is as follows:

```
for variable in iterable:
    # Code to be executed in each iteration
    # This code block is indented and continues for each item in the iterable
    # You can have multiple statements inside the loop

```

Components breakdown:

- `for`: This keyword is used to start a for loop.
- `variable`: This is a variable that takes on the value of each item in the iterable during each iteration of the loop.
- `in`: This keyword is used to specify the iterable (e.g., a list, tuple, string, etc.) over which you want to iterate.
- `iterable`: This is the collection or sequence of items that you want to loop through.
- `:` (colon): It signifies the start of a new block of code, and all statements inside the loop must be indented to the same level.

Example of a for loop that prints the lowest number in the list:

```
num_list = [13, 42, 10, 100, 30, 55, 111, 20, 23, 70, 95, 2]

# Initialize a variable to store the minimum value
min_num = num_list[0]

# Start the loop from the second element in the list (index 1)
for num in num_list:
    # Check if the current element is less than the current minimum
    if num < min_num:
        min_num = num # Update the minimum value

# Print the lowest number found in the list
print("The lowest number in the list is: ", min_num)
```
