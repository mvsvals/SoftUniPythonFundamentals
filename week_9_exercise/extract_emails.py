# Write a program that receives a single string and extracts all email addresses from it.
# Print the extracted email addresses on separate lines. Emails are in the format "{user}@{host}", where:
#     • {user} could consist only of letters and digits; the symbols ".", "-" and "_" can appear between them.
#         ◦ Examples of valid users: "stephan", "mike03", "s.johnson", "st_steward", "softuni-bulgaria", "12345"
#         ◦ Examples of invalid users: ''--123", ".....", "nakov_-", "_steve", ".info"
#     • {host} is a sequence of at least two words, each couple of words must be separated by a single dot ".". Each word consists of letters. There can be hyphens "-" between the letters, except for the last word.
#         ◦ Examples of valid hosts: "softuni.bg", "software-university.com", "intoprogramming.info", "mail.softuni.org"
#         ◦ Examples of invalid hosts: "helloworld", ".unknown.soft." , "invalid-host-", "invalid-"
import re

input_email_string = input()
pattern = r'\s([a-z0-9]+[\.\-_]*[a-z0-9]*@(?:[a-z]+\-?[a-z]*\.)+[a-z]+)\b'

matches = re.findall(pattern, input_email_string)

for match in matches:
    print(match)