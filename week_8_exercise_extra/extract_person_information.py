
# Example: "Hello my name is @Peter| and I am #20* years old."
# For each found name-age pair, print a line in the following format "{name} is {age} years old."

def locate_data(type: str, raw_input: str) -> str:
    if type == 'name':
        start_sign = '@'
        end_sign = '|'
    elif type == 'age':
        start_sign = '#'
        end_sign = '*'
    start_index = raw_input.find(start_sign) + 1
    end_index = raw_input.find(end_sign)
    output_data = raw_input[start_index:end_index]
    return output_data

total_lines = int(input())

for string in range(total_lines):
    input_string = input()
    print(f"{locate_data('name', input_string)} is {locate_data('age', input_string)} years old.")

