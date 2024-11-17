player_db = {}

while True:
    input_string = input()
    if input_string == 'Season end':
        break

    if ' -> ' in input_string:
        player, position, skill = input_string.split(' -> ')
        skill = int(skill)

        if player not in player_db:
            player_db[player] = {}
        if position not in player_db[player] or player_db[player][position] < skill:
            player_db[player][position] = skill

    elif ' vs ' in input_string:
        player_one, player_two = input_string.split(' vs ')
        if player_one in player_db and player_two in player_db:
            have_common_positions = False
            for position in player_db[player_one]:
                if position in player_db[player_two]:
                    have_common_positions = True
                    break

            if have_common_positions:
                total_skill_one = sum(player_db[player_one].values())
                total_skill_two = sum(player_db[player_two].values())

                if total_skill_one > total_skill_two:
                    del player_db[player_two]
                elif total_skill_one < total_skill_two:
                    del player_db[player_one]

total_skill = {}
for player in player_db:
    total_points_for_player = sum(player_db[player].values())
    total_skill[player] = total_points_for_player

for player, skill in sorted(total_skill.items(), key=lambda x: (-x[1], x[0])):
    print(f"{player}: {skill} skill")
    for position, position_skill in sorted(player_db[player].items(), key=lambda x: (-x[1], x[0])):
        print(f'- {position} <::> {position_skill}')
