# On the first line, you will receive a number n.
# On the second line, you will receive a word.
# On the following n lines, you will be given some strings.
# You should add them to a list and print them.
# After that, you should filter out only the strings that include the given word and print that list too.


input_number = int(input())
input_word = input()
my_list = []
filtered_list = []

for _ in range(input_number):
    list_element = input()
    my_list.append(list_element)
    if input_word in list_element:
        filtered_list.append(list_element)
print(my_list)
print(filtered_list)