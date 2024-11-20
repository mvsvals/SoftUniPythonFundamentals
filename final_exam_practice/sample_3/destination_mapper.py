import re

valid_locations = []
total_points = 0

input_data = input()
pattern= r'(=|\/)([A-Z][a-zA-Z]{2,})\1'
match = re.findall(pattern, input_data)
valid_locations = [location[1] for location in match]

if valid_locations:
    total_points = sum(len(x) for x in valid_locations)

print('Destinations:',', '.join(valid_locations))
print(f'Travel Points: {total_points}')