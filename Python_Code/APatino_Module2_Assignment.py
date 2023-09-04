# Problem 1
s = "Programming Python"

# a. Three ways to get the Letter "P" using the index operator

# Prints the letter "P" from the word Programming, using a positive index
first_p = s[0]
print(first_p)

# Prints the letter "P" from the word Python, using a negative index
second_p = s[-6]
print(second_p)

# Prints the letter "P" from the word Python, using the index() method
# Finds the index of the first ocurrance of P which is 0
index_p = s.index("P")
p_letter = s[index_p]
print(p_letter)

# b. Two ways to get the slice, "Python"

# Prints Python by specifyng the start offset to the end offset minus 1 using positive indexes for slices
print(s[12:18])

# Prints Python by specifying the start offset to the end using negative indexes for slices
print(s[-6:])


# Problem 2
string = "   I am    Programming    Python!       "

# Splitted the string into individual words using the whitespace as the delimiter
words = string.split()

# Join the words using a single space as the separator
new_string = " ".join(words)

print(new_string)


# Problem 3
length = 5
width = 2.5
height = 2.73

volume = length * width * height

string = f"The box has a length: {length}, width: {width} and height: {height}. The volume is: {volume:.1f}."

print(string)


# Problem 4
original_list = [1, 2, 3, 4, 5, 6, 7, 8]

# a
# deleted each number that did not exist in the wanted list from the original list
del original_list[0]
del original_list[1]
del original_list[2]
del original_list[3]
# created a list with the numbers that existed in the wanted list but were missing from the origional list
additional_list = [10, 12, 14]
# Joined the two lists
new_list = original_list + additional_list
# I assigned the values of the new list to the variable original list
original_list = new_list
print(original_list)

# b
og_list = [1, 2, 3, 4, 5, 6, 7, 8]

og_list.remove(1)
og_list.remove(3)
og_list.remove(5)
og_list.remove(7)
og_list.append(10)
og_list.append(12)
og_list.append(14)

print(og_list)


# Problem 5
t = ('anita', 0, 'brandon', 'chitra', 5, 7)

# Used tuple comprehension to iterate through each element of the original tuple t.
# If the element is a string (checked using isinstance(word, str)), it's capitalized using the capitalize() method.
# Numeric items and non-string items are skipped.
corrected_t = tuple(word.capitalize() for word in t if isinstance(word, str))

# Assigned t to the new tuple that was created
t = corrected_t

print(t)
