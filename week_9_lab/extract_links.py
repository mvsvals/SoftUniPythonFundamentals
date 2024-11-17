import re

input_text = input()
pattern = r'www\.[a-zA-Z0-9\-]+(?:\.[a-z]+)+'
valid_emails = []

while input_text:
    match = re.findall(pattern, input_text)
    if match:
        valid_emails += match
    input_text = input()

for email in valid_emails:
    print(email)