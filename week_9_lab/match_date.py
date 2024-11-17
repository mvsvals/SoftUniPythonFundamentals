import re

pattern = r'(^|(?<=\s))'
text = input()

matches = re.findall(pattern, text)
for match in matches:
    print(f'Day: {match[0]}, Month: {match[2]}, Year: {match[3]}')
