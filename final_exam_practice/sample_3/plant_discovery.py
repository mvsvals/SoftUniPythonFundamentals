
total_lines = int(input())
plant_dict = {}
rating_dict = {}

for x in range(total_lines):
    plant, rarity = input().split('<->')
    plant_dict[plant] = rarity
    rating_dict[plant] = []

while True:
    input_string = input()
    if input_string == 'Exhibition':
        break
    command, argument = input_string.split(": ")
    if command == 'Rate':
        plant, rating = argument.split(' - ')
        if plant in plant_dict:
            rating_dict[plant].append(int(rating))
        else:
            print("error")
    elif command == 'Update':
        plant, new_rarity = argument.split(' - ')
        if plant in plant_dict:
            plant_dict[plant] = new_rarity
        else:
            print("error")
    elif command == 'Reset':
        plant = argument
        if plant in plant_dict:
            rating_dict[plant] = []
        else:
            print("error")

print("Plants for the exhibition: ")

for plant in plant_dict:
    if len(rating_dict[plant]) < 1:
        average_rating = 0.00
    else:
        average_rating = sum(rating_dict[plant]) / len(rating_dict[plant])
    print(f'- {plant}; Rarity: {plant_dict[plant]}; Rating: {average_rating:.2f}')