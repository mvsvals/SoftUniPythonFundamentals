contests_dict = {}
user_dict = {}

while True:
    input_string = input()
    if input_string == 'end of contests':
        break
    contest, password = input_string.split(':')
    contests_dict[contest] = password

while True:
    input_string = input()
    if input_string == 'end of submissions':
        break
    contest, password, username, points = input_string.split('=>')
    if contest in contests_dict.keys() and password == contests_dict[contest]:
        if username not in user_dict.keys():
            user_dict[username] = {}
        if contest not in user_dict[username].keys():
            user_dict[username][contest] = 0
        if int(points) > user_dict[username][contest]:
            user_dict[username][contest] = int(points)

best_candidate = ['', 0]

for user in user_dict.keys():
    user_total_points = sum(user_dict[user].values())
    if user_total_points > best_candidate[1]:
        best_candidate = [user, user_total_points]

print(f"Best candidate is {best_candidate[0]} with total {best_candidate[1]} points.")
print('Ranking:')
for user in sorted(user_dict.keys()):
    print(user)
    for contest, grade in sorted(user_dict[user].items(), key=lambda item: item[1], reverse=True):
        print('#  ' + contest + ' -> ' + str(grade))
