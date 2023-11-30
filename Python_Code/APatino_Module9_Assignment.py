import re

# Problem 1

pattern = r'\b(?:[A-Z]{2,}|[a-z]{2,})\w*\b'

# Test cases
test_strings = ['UCX', 'AM', 'PM', 'hello', 'University', 'Programming']

for test_str in test_strings:
    if re.match(pattern, test_str):
        print(f'Match: {test_str}')
    else:
        print(f'No match: {test_str}')


# Problem 2
file_content = ''' 
# this is a comment
print("hello world") # this is another comment
'''


def remove_comments(file_content):
    # Use regular expression to remove comments
    content_without_comments = re.sub(r'#.*', '', file_content)

    return content_without_comments


# Example usage:
result = remove_comments(file_content)
print(result)


# Problem 3
def find_valid_emails(file_content):
    # Regular expression for valid email addresses
    email_pattern = re.compile(
        r'\b[A-Za-z0-9_.+-]+@[A-Za-z0-9-]+\.[A-Za-z]{2,}\b')

    # Find all matches in the content
    matches = email_pattern.findall(file_content)

    return matches


# Example usage:
file_content = '''
Email addresses sample:
john.doe@example.com
alice_smith123@gmail.com
info@company-xyz.com
user123@domain.co.uk
Invalid Email: thisisnotanemail
Another one: john.doe@com
'''

valid_emails = find_valid_emails(file_content)

# Print the valid email addresses
for email in valid_emails:
    print(email)


# Problem 4
def standardize_phone_numbers(text):
    # Regular expression for matching and capturing phone number components
    phone_pattern = re.compile(
        r'\(?\b(\d{3})\)?[.-]?\s?(\d{3})[.-]?\s?(\d{4})\b')

    # Replace matched phone numbers with the standardized format
    result = re.sub(phone_pattern, r'\1-\2-\3', text)

    return result


# Example usage:
phone_numbers = [
    "(415)555-1212",
    "510-778-1234",
    "408 555 4321",
    "650.444.1213"
]

# Standardize and print the phone numbers
for phone_number in phone_numbers:
    standardized_number = standardize_phone_numbers(phone_number)
    print(standardized_number)
