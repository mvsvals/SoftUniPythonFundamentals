# Write a program to read an integer N and print all triples of the first N small Latin letters, ordered alphabetically:

input_number = int(input())

for i in range(0, input_number):
    for k in range(0, input_number):
        for l in range(0, input_number):
            print(f'{chr(97 + i)}{chr(97 + k)}{chr(97 + l)}')

