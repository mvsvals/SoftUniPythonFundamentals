# Create a program that helps you plan the gifts for your friends and family.
# First, you are going to receive the gifts you plan on buying on a single line, separated by space, in the following format:
# "{gift1} {gift2} {gift3}… {giftn}"
# Then you will start receiving commands until you read the "No Money" message. There are three possible commands:
#     • "OutOfStock {gift}"
#         ◦ Find the gifts with this name in your collection, if any, and change their values to "None".
#     • "Required {gift} {index}"
#         ◦ If the index is valid, replace the gift on the given index with the given gift.
#     • "JustInCase {gift}"
#         ◦ Replace the value of your last gift with this one.
# In the end, print the gifts on a single line, except the ones with the value "None", separated by a single space in the following format:
# "{gift1} {gift2} {gift3} … {giftn}"

input_gifts = input().split()

while True:
    input_command = input()
    if input_command == 'No Money':
        break
    input_command = input_command.split()
    if input_command[0] == 'OutOfStock':
        for i in range(len(input_gifts)):
            if input_gifts[i] == input_command[1]:
                input_gifts[i] = None
    elif input_command[0] == 'Required':
        index = int(input_command[2])
        if index < len(input_gifts):
            input_gifts[index] = input_command[1]
    elif input_command[0] == 'JustInCase':
        input_gifts[-1] = input_command[1]

output_list = []
for gift in input_gifts:
    if gift is not None:
        output_list.append(gift)

print(*output_list)