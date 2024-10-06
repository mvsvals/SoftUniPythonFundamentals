# You will receive a single integer number between 0 and 100 (inclusive) divisible by 10 without remainder (0, 10, 20, 30...).
# Your task is to create a function that returns a loading bar depending on the number you have received in the input.
# Print the result on the console.

# 30	30% [%%%.......]
# Still loading...
# 50	50% [%%%%%.....]
# Still loading...
# 100	100% Complete!
# [%%%%%%%%%%]


def loading_bar(number: int) -> list[str]:
    percentages_to_print = int(number)
    dots_to_print = int(10 - input_loading_progress)
    return '[' + f'{"%" * percentages_to_print + "." * dots_to_print}' + ']'


input_loading_progress = int(input()) / 10

if input_loading_progress != 10:
    print(f'{int(input_loading_progress * 10)}% ' + loading_bar(input_loading_progress))
    print('Still loading...')
else:
    print(f'{int(input_loading_progress * 10)}% ' + 'Complete!')
    print(loading_bar(input_loading_progress))
