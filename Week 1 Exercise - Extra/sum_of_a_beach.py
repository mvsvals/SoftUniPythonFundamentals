# Beaches are filled with sand, water, fish, and sun. Given a string, calculate how many times the words "Sand", "Water", "Fish", and "Sun" appear (case insensitive).
#
# Examples
# Input Output
# WAtErSlIde 1
# GolDeNSanDyWateRyBeaChSuNN 3
# gOfIshsunesunFiSh 4
# cItYTowNcARShoW 0

input_string = input().lower()
target_words = ['sand', 'water', 'fish', 'sun']
total_target_words = 0

for word in target_words:
    total_target_words += input_string.count(word)

print(total_target_words)





