
remaining_energy: int = int(input())
battles_won = 0

while True:
    input_command = input()
    if input_command == 'End of battle':
        print(f"Won battles: {battles_won}. Energy left: {remaining_energy}" )
        break
    distance_to_enemy = int(input_command)
    if remaining_energy >= distance_to_enemy:
        remaining_energy -= distance_to_enemy
        battles_won += 1
        if (battles_won % 3 == 0) and battles_won != 0:
            remaining_energy += battles_won
    else:
        print(f"Not enough energy! Game ends with {battles_won} won battles and {remaining_energy} energy")
        break


