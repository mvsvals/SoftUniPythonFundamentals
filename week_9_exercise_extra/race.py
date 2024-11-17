import re

race_participants = {person: 0 for person in input().split(', ')}

while True:
    input_data = input()
    if input_data == 'end of race':
        break
    person_pattern = '[a-zA-Z]+'
    distance_pattern = r'\d'
    person_name = ''.join(re.findall(person_pattern, input_data))
    if person_name in race_participants:
        distance = re.findall(distance_pattern, input_data)
        total_distance = sum(int(x) for x in distance)
        race_participants[person_name] += total_distance

race_participants = sorted(race_participants.items(), key= lambda x: x[1], reverse=True)
print(f'1st place: {race_participants[0][0]}')
print(f'2nd place: {race_participants[1][0]}')
print(f'3rd place: {race_participants[2][0]}')
