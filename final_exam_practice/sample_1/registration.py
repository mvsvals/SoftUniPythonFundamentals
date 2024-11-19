# On the first line, you will receive the username that he wants to use in the first place.
# On the following lines, you will be receiving commands until the "Registration" command. There are five possible commands:
#     • "Letters {Lower/Upper}"
#         ◦ Replace all letters with lower case or with upper case, then print the result.
#     • "Reverse {startIndex} {endIndex}"
#         ◦ Reverse the substring from the start index until the end index (both inclusive), then print it. Do NOT change it in the username.
# Note: Check if the indices are valid. If they aren't - skip the command. An index is valid when it is non-negative and less than the size of the collection.
#     • "Substring {substring}"
#         ◦ If the username contains the given substring, cut it out and print the result without the cut substring.
#         ◦ Otherwise, print:
# "The username {string} doesn't contain {substring}."
#     • "Replace {char}"
#         ◦ Replace all occurences of the given char with a dash (-) and print the result.
#     • "IsValid {char}"
#         ◦ For a username to be valid, it must contain the given char. If it is, print "Valid username.".
#         ◦ Otherwise, print: "{char} must be contained in your username."
# Input
#     • On the first line, you are going to receive the string.
#     • On the following lines, until the "Registration" command is received, you will be receiving commands.
#     • All commands are case-sensitive.
# Output
#     • Print the output of every command in the format described above.


username = input()

while True:
    input_string = input()
    if input_string == 'Registration':
        break
    input_command = input_string.split()
    if input_command[0] == 'Letters':
        if input_command[1] == 'Lower':
            username = username.lower()
        elif input_command[1] == 'Upper':
            username = username.upper()
        print(username)
    elif input_command[0] == 'Reverse':
        start_index = int(input_command[1])
        end_index = int(input_command[2])
        if 0 <= start_index < len(username) and 0 <= end_index < len(username):
            print(username[start_index:end_index+1][::-1])
    elif input_command[0] == 'Substring':
        if input_command[1] in username:
            username = username.replace(input_command[1], '')
            print(username)
        else:
            print(f"The username {username} doesn't contain {input_command[1]}.")
    elif input_command[0] == 'Replace':
        username = username.replace(input_command[1], '-')
        print(username)
    elif input_command[0] == 'IsValid':
        char = input_command[1]
        if char in username:
            print("Valid username.")
        else:
            print(f'{char} must be contained in your username.')