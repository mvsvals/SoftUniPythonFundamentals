# You will receive a field of a tic-tac-toe game in three lines containing numbers, separated by a single space.
# Legend:
#     • 0 - empty space
#     • 1 - first player move
#     • 2 - second player move
# Find out who the winner is. If the first player wins, print "First player won". If the second player wins, print "Second player won". Otherwise, print "Draw!".

horizontal_line_one = list(map(int, input().split()))
horizontal_line_two = list(map(int, input().split()))
horizontal_line_three = list(map(int, input().split()))
vertical_line_one = [horizontal_line_one[0], horizontal_line_two[0], horizontal_line_three[0]]
vertical_line_two = [horizontal_line_one[1], horizontal_line_two[1], horizontal_line_three[1]]
vertical_line_three = [horizontal_line_one[2], horizontal_line_two[2], horizontal_line_three[2]]

player_one_won = (horizontal_line_one.count(1) == 3) or \
                 (horizontal_line_two.count(1) == 3) or \
                 (horizontal_line_three.count(1) == 3) or \
                 (vertical_line_one.count(1) == 3) or \
                 (vertical_line_two.count(1) == 3) or \
                 (vertical_line_three.count(1) == 3) or \
                 (horizontal_line_one[0] == 1 and horizontal_line_two[1] == 1 and horizontal_line_three[2] == 1) or \
                 (horizontal_line_one[2] == 1 and horizontal_line_two[1] == 1 and horizontal_line_three[0] == 1)


player_two_won = (horizontal_line_one.count(2) == 3) or \
                 (horizontal_line_two.count(2) == 3) or \
                 (horizontal_line_three.count(2) == 3) or \
                 (vertical_line_one.count(2) == 3) or \
                 (vertical_line_two.count(2) == 3) or \
                 (vertical_line_three.count(2) == 3) or \
                 (horizontal_line_one[0] == 2 and horizontal_line_two[1] == 2 and horizontal_line_three[2] == 2) or \
                 (horizontal_line_one[2] == 2 and horizontal_line_two[1] == 2 and horizontal_line_three[0] == 2)

if not (player_two_won or player_one_won):
    print('Draw!')
elif player_one_won:
    print('First player won')
elif player_two_won:
    print('Second player won')