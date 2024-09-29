# The rules: Two teams, named "A" and "B" have 11 players each.
# The players on each team are numbered from 1 to 11.
# Any player may be sent off the field by being given a red card.
# If one of the teams has less than 7 players remaining, the referee stops the game immediately, and the team with less than 7 players loses.
# The card is a string with the team's letter ("A" or "B") followed by a single dash and the player's number. e.g., the card "B-7" means player #7 from team B received a card.
# The task: You will be given a sequence of cards (could be empty), separated by a single space. You should print the count of remaining players on each team at the end of the game in the format: "Team A - {players_count}; Team B - {players_count}". If the referee terminated the game, print an additional line: "Game was terminated".
# Note for the random tests: If a player who has already been sent off receives another card - ignore it.

input_card_list = input().split()
team_a_remaining_players = [f"A-{number}" for number in range(1, 12)]
team_b_remaining_players = [f"B-{number}" for number in range(1, 12)]
is_game_terminated = False

for card in input_card_list:
    if card in team_a_remaining_players:
        team_a_remaining_players.remove(card)
    elif card in team_b_remaining_players:
        team_b_remaining_players.remove(card)
    if len(team_a_remaining_players) < 7 or len(team_b_remaining_players) < 7:
        is_game_terminated = True
        break

print(f'Team A - {len(team_a_remaining_players)}; Team B - {len(team_b_remaining_players)}')
if is_game_terminated:
    print("Game was terminated")


