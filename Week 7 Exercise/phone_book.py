# Write a program that receives info from the console about people and their phone numbers.
# Each entry should have a name and a number (both strings) separated by a "-".
# If you receive a name that already exists in the phonebook, update its number.
# After filling out the phonebook, you will receive a number – N.
# Your program should be able to perform a search of contact by name and print its details in the format: "{name} -> {number}".
# In case the contact isn't found, print: "Contact {name} does not exist."

phone_book = {}
total_searches = 0

while True:
    input_string = input()
    if input_string.isdigit():
        total_searches = int(input_string)
        break
    name, phone_number = input_string.split('-')
    phone_book[name] = phone_number

for i in range(total_searches):
    search_string = input()
    if search_string in phone_book.keys():
        print(f'{search_string} -> {phone_book[search_string]}')
    else:
        print(f'Contact {search_string} does not exist.')