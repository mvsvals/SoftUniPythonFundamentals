# Until you receive the command "END", you need to read commands on different lines.
# According to the commands, calculate the number of coffees you need to drink to stay awake during the daytime.
# The list of events can contain the following:
#     • You have homework to do ("coding").
#     • You have a dog or a cat that decided to wake you up too early ("dog" or "cat").
#     • You watch a movie ("movie").
#     • If other events are present, they will be represented by arbitrary strings. Just ignore them!
# Each event can be lowercase or uppercase:
#     • If it is lowercase, you need 1 coffee by an event.
#     • If it is uppercase, you need 2 coffees by an event.
# In the end, print the number of coffees you will need. If the count has exceeded 5, just print "You need extra sleep".

total_coffee_needed = 0

while True:
    input_command = input()
    if input_command == 'END':
        break
    input_command_lower = input_command.lower()
    if input_command_lower == 'coding' or input_command_lower == 'dog' or input_command_lower == 'cat' or input_command_lower == 'movie':
        if input_command.islower():
            total_coffee_needed += 1
        elif input_command.isupper():
            total_coffee_needed += 2


if total_coffee_needed > 5:
    print('You need extra sleep')
else:
    print(total_coffee_needed)

