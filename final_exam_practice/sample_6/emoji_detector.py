
import re

cool_emojis = []

raw_emoji_data = input()
valid_emoji_pattern = r'((::|\*\*)([A-Z][a-z]{2,})\2)'
coolness_threshold_pattern = r'\d'

coolness_threshold_matches = re.findall(coolness_threshold_pattern, raw_emoji_data)
coolness_threshold = 1

for match in coolness_threshold_matches:
        coolness_threshold *= int(match)

print(f"Cool threshold: {coolness_threshold}")

valid_emoji_matches = re.findall(valid_emoji_pattern, raw_emoji_data)

print(f"{len(valid_emoji_matches)} emojis found in the text. The cool ones are:")
for emoji in valid_emoji_matches:
    coolness = sum(ord(x) for x in emoji[2])
    if coolness > coolness_threshold:
        cool_emojis.append(emoji[0])

for cool_emoji in cool_emojis:
    print(cool_emoji)

