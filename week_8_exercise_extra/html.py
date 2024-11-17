# You will receive lines of input:
#     • On the first line, you will receive a title of an article
#     • On the second line, you will receive the content of that article
#     • On the following lines, until you receive "end of comments" you will get the comments about the article
# Print the whole information in HTML format:
#     • The title should be in "h1" tag (<h1></h1>)
#     • The content in article tag (<article></article>)
#     • Each comment should be in div tag (<div></div>)
# For more clarification see the example below.

article_title = input()
article_content = input()
article_comments = []

while True:
    input_string = input()
    if input_string == 'end of comments':
        break
    article_comments.append(input_string)

print(f'<h1>\n\t{article_title}\n</h1>')
print(f'<article>\n\t{article_content}\n</article>')
for comment in article_comments:
    print(f'<div>\n\t{comment}\n</div>')


