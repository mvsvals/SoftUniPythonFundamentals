# Write a program that reads usernames on a single line (separated by ", ") and prints all valid usernames on separate lines.
# A valid username:
#     • has length between 3 and 16 characters inclusive
#     • can contain only letters, numbers, hyphens, and underscores
#     • has no redundant symbols before, after, or in between

input_usernames = [username for username in input().split(", ") if 3 <= len(username) <= 16]
additional_allowed_chars = ['-', '_']


for username in input_usernames:
    is_valid_username = True
    for char in username:
        if not char.isalnum() and char not in additional_allowed_chars:
            is_valid_username = False
            break
    if is_valid_username:
        print(username)


