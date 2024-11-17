import re

pattern = r'(?:^|\s)\+359([ -])2\1\d{3}\1\d{4}\b'
text = input()

matches = [match.group().strip() for match in re.finditer(pattern, text)]

print(*matches, sep=", ")
1 -1 1s 123 s-s -123 _55_ _f 123.456 -123.456 s-1.1 s2 -1- zs-2 s-3.5 00.5
