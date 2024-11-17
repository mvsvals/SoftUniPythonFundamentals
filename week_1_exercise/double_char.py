# You will be given strings until you receive the command "End".
# For each string given, you should print a string in which each character (case-sensitive) is repeated twice.
# Note that if you receive the string "SoftUni", you should NOT print it!


while True:
    input_string = input()
    if input_string == "End":
        break
    elif input_string == "SoftUni":
        continue
    for char in input_string:
        print(char * 2, end='')
    print()





