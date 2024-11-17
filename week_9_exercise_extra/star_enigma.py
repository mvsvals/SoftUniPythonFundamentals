import re

key_letters = ['s', 't', 'a', 'r']

total_messages = int(input())
attacked_planets, destroyed_planets = [], []

for message in range(total_messages):
    encrypted_message = input()
    key_letter_total_count = sum(encrypted_message.lower().count(x) for x in key_letters)
    decrypted_message = ''
    for letter in encrypted_message:
        new_letter_ascii = ord(letter) - key_letter_total_count
        decrypted_message += chr(new_letter_ascii)
    # print(decrypted_message)
    pattern = r'.*?@([A-Za-z]+)[^@:!\->]*:(\d+)[^@:!\->]*!([AD])![^@:!\->]*->(\d+)'
    match = re.findall(pattern, decrypted_message)
    if match:
        attack_type = match[0][2]
        plane_name = match[0][0]
        if attack_type == 'D':
            destroyed_planets.append(plane_name)
        elif attack_type == 'A':
            attacked_planets.append(plane_name)

print(f'Attacked planets: {len(attacked_planets)}')
if len(attacked_planets) > 0:
    attacked_planets.sort()
    for planet in attacked_planets:
        print(f"-> {planet}")

print(f'Destroyed planets: {len(destroyed_planets)}')
if len(destroyed_planets) > 0:
    destroyed_planets.sort()
    for planet in destroyed_planets:
        print(f"-> {planet}")

