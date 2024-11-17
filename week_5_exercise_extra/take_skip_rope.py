
input_string = input()
result_string = []

digit_list = [int(digit) for digit in input_string if digit.isdigit()]
alpha_or_ascii_list = [alpha_or_ascii for alpha_or_ascii in input_string if not alpha_or_ascii.isdigit()]

# even index
take_list = [int(digit) for index, digit in enumerate(digit_list) if index % 2 == 0]
# odd index
skip_list = [int(digit) for index, digit in enumerate(digit_list) if index % 2 != 0]

for action in range(len(take_list)):
    result_string += alpha_or_ascii_list[:take_list[action]]
    alpha_or_ascii_list[:take_list[action]] = []
    alpha_or_ascii_list[:skip_list[action]] = []

print(*result_string, sep='')

