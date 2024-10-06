# Write a function that checks if a given password is valid. Password validations are:
#     • It should be 6 - 10 (inclusive) characters long
#     • It should consist only of letters and digits
#     • It should have at least 2 digits
# If a password is valid, print "Password is valid".
# Otherwise, for every unfulfilled rule, print a message:
#     • "Password must be between 6 and 10 characters"
#     • "Password must consist only of letters and digits"
#     • "Password must have at least 2 digits"

errors = []
def check_password_validity(password: str) -> str:
    if len(password) > 10 or len(password) < 6:
        errors.append('Password must be between 6 and 10 characters')
    if not password.isalnum():
        errors.append('Password must consist only of letters and digits')
    digit_counter = sum(1 for char in password if char.isdigit())
    if digit_counter < 2:
        errors.append('Password must have at least 2 digits')

    if not errors:
        return 'Password is valid'
    else:
        return '\n'.join(errors)

input_password = input()
print(check_password_validity(input_password))

