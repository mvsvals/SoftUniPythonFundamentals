# Write a program that extracts a title and all the content of an HTML file:
#     • The title should be between the HTML tags <title> and </title>.
#     • The content should be between the HTML tags <body> and </body>.
# There might be different HTML tags, which you should ignore:
#     • Each HTML tag is surrounded by the symbols "<" and ">". For example: <body>, <p>, </html>
#     • You also should ignore the HTML tag "\n"
# Example:
# "<html>\n<head><title>News</title></head>\n<body><p><a href="https://softuni.bg">SoftUni</a>aims to provide free real-world practical\n training for young people who want to turn into\n skillful Python software engineers.</p></body>\n</html>"
# In this example the title is "News" and the content is "SoftUni aims to provide free real-world practical training for young people who want to turn into skillful Python software engineers."
# Input

import re

html_input_line = input()

title_pattern = r'<title>(.+)<\/title>'
title = re.findall(title_pattern, html_input_line)

print(f'Title: {title[0]}')

body_pattern = r'<body>(.+)<\/body>'
body = re.findall(body_pattern, html_input_line)
body = body[0]

replacement_pattern = r'<[a-z]+[ a-z=\":\/\.]*>|<\/[a-z]*[ a-z=\":\/\.]+>|\\n'
content = re.sub(replacement_pattern, '', body)
print(f'Content: {content}')




