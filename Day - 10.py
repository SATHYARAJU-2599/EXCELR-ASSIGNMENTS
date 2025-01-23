import re

def extract_emails(text):
    # Regular expression pattern for extracting email addresses
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    # Find all matches of the pattern in the given text
    emails = re.findall(email_pattern, text)
    return emails

# Test the function with the given input
test_input = 'Contact us at support@example.com and sales@example.org.'
result = extract_emails(test_input)
print("Original Text:", test_input)
print("Extracted Emails:", result)
