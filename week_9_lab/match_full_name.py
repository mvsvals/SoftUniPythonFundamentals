import re

match_string = input()
pattern = r'\b[A-Z][a-z]+\b \b[A-Z][a-z]+\b'

match = re.findall(pattern, match_string)

print(' '.join(match))