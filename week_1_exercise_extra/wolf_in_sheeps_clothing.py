input_string = input()
animal_list = input_string.split(", ")

wolf_location = animal_list.index('wolf')
if wolf_location == len(animal_list) - 1:
    print("Please go away and stop eating my sheep")
else:
    sheep_position = len(animal_list) - 1 - int(wolf_location)
    print(f"Oi! Sheep number {sheep_position}! You are about to be eaten by a wolf!")