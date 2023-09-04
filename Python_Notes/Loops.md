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

## Nested Loops

- Nested loops are loops that are placed inside other loops
- The nested loop consists of an outer loop and one or more inner loops
  - Outer Loop: The outer loop is responsible for controlling the execution of the inner loop(s). It runs from its starting point to its ending point, and each time it iterates, it triggers the inner loop(s).
  - Inner Loop(s): The inner loop(s) are executed once for each iteration of the outer loop. They have their own loop variables and control structures. The inner loop(s) complete their full cycle for each iteration of the outer loop.
- Nested loops are used to work with:
  - multi-dimensional data structures (matrices or grids)
  - examine combinations
  - permutations of elements from different collections

Standard and most common nested loop syntax:

```
for outer_variable in outer_range:
    # Outer loop code

    for inner_variable in inner_range:
        # Inner loop code

```

Components breakdown:

- `for outer_variable in outer_range:`: This is the outer loop declaration. It specifies the loop variable (outer_variable) and the range or iterable (outer_range) that the outer loop will iterate over.
- `# Outer loop code`: This is the code block that is executed for each iteration of the outer loop. You can place any statements or code inside this block.
- `for inner_variable in inner_range:`: This is the inner loop declaration. It specifies the loop variable (inner_variable) and the range or iterable (inner_range) that the inner loop will iterate over.
- `# Inner loop code`: This is the code block that is executed for each iteration of the inner loop. It is placed inside the outer loop, so it will run for each combination of the outer loop and inner loop.

Example of a nested loop that finds as many unique pairs of integer numbers whose product is 120:

```
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

```
