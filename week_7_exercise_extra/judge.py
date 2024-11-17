contest_dict = {}
individual_standing = {}

while True:
    input_string = input()

    if input_string == 'no more time':
        break

    username, contest, points = input_string.split(' -> ')
    points = int(points)

    if username not in individual_standing.keys():
        individual_standing[username] = 0

    if contest not in contest_dict.keys():
        contest_dict[contest] = {}

    if username not in contest_dict[contest]:
        contest_dict[contest][username] = 0

    if contest_dict[contest][username] < points:
        contest_dict[contest][username] = points


for contest in contest_dict.keys():
    print(f'{contest}: {len(contest_dict[contest])} participants')
    user_pos = 1

    for user, score in sorted(contest_dict[contest].items(), key=lambda x: (-x[1], x[0])):
        print(f'{user_pos}. {user} <::> {score}')
        user_pos += 1
        individual_standing[user] += int(score)

user_pos = 1
print("Individual standings:")
for user, score in sorted(individual_standing.items(), key=lambda x: (-x[1], x[0])):
    print(f'{user_pos}. {user} -> {score}')
    user_pos += 1
