# Write a function that, depending on the first line of the input, reads one of the following strings: "int", "real", or "string".
#     • If the data type is an int, multiply the number by 2.
#     • If the data type is real, multiply the number by 1.5 and format the result to the second decimal point.
#     • If the data type is a string, surround the input with "$".
# Print the result on the console.

input_data_type = input()
input_data_amount = input()

def data_processing(type: str, amount: float):
    if type == 'int':
        return int(amount) * 2
    elif type == 'real':
        return f'{float(amount) * 1.5:.2f}'
    elif type == 'string':
        return '$' + f'{amount}' + '$'



print(data_processing(input_data_type, input_data_amount))