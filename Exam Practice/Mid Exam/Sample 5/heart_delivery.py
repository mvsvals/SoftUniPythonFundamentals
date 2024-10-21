hearts_needed = [int(number) for number in input().split('@')]
cupid_index = 0

while True:
    input_command = input().split()
    if input_command[0] == "Love!":
        break
    elif input_command[0] == 'Jump':
        length = int(input_command[1])
        if cupid_index + length > len(hearts_needed) - 1:
            cupid_index = 0
        else:
            cupid_index += length
        if hearts_needed[cupid_index] == 0:
            print(f'Place {cupid_index} already had Valentine\'s day.')
        else:
            hearts_needed[cupid_index] -= 2
            if hearts_needed[cupid_index] <= 0:
                print(f'Place {cupid_index} has Valentine\'s day.')

print(f"Cupid's last position was {cupid_index}.")
all_had_valentines_days = hearts_needed.count(0) == len(hearts_needed)
if all_had_valentines_days:
    print("Mission was successful.")
else:
    print(f"Cupid has failed {len(hearts_needed) - hearts_needed.count(0)} places.")

