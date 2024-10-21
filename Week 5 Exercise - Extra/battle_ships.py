
# After that, you will receive the squares that are being attacked in the format: "{row}-{col} {row}-{col}".
# Each time a square is being attacked, if there is a ship (number greater than 0), you should reduce its value by 1.
# If a ship's health reaches zero, it is destroyed. After the attacks have ended, print how many ships were destroyed.

total_rows = int(input())
game_board = []
total_ships_destroyed = 0

for row in range(total_rows):
    input_row = input().split()
    game_board.append(list(map(int, input_row)))

attacks_input = input().split()
for i in range(len(attacks_input)):
    command_split = attacks_input[i].split('-')
    x = int(command_split[0])
    y = int(command_split[1])
    if int(game_board[x][y]) > 0:
        game_board[x][y] -= 1
        if int(game_board[x][y]) == 0:
            total_ships_destroyed += 1

print(total_ships_destroyed)