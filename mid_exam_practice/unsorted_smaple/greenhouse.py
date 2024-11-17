
crops = input().split(' & ')

while True:
    input_command = input()
    if input_command == 'Collect!':
        break
    input_command = input_command.split()
    command = input_command[0]
    if command == 'Plant':
        crop = input_command[1]
        if crop not in crops:
            crops.insert(0, crop)
    elif command == 'Transplant':
        crop = input_command[1]
        if crop in crops:
            crops.append(crop)
            crops.remove(crop)
    elif command == 'Replace':
        crop_index_one = int(input_command[1])
        crop_index_two = int(input_command[2])
        if 0 <= crop_index_one <= len(crops) - 1 and 0 <= crop_index_two <= len(crops) - 1:
            crops[crop_index_one], crops[crop_index_two] = crops[crop_index_two], crops[crop_index_one]
    elif command == 'Uproot':
        crop = input_command[1]
        if crop in crops:
            crops.remove(crop)

print(*crops, sep=" | ")