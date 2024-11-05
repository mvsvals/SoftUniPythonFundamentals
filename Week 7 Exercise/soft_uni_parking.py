
number_of_commands = int(input())
license_plate_dict = {}

for command in range(number_of_commands):
    input_command = input().split()
    if input_command[0] == 'register':
        username, license_plate_number = input_command[1:]
        if username in license_plate_dict:
            print(f"ERROR: already registered with plate number {license_plate_dict[username]}")
        else:
            print(f"{username} registered {license_plate_number} successfully")
            license_plate_dict[username] = license_plate_number
    elif input_command[0] == 'unregister':
        username = input_command[1]
        if username not in license_plate_dict.keys():
            print(f"ERROR: user {username} not found")
        else:
            print(f"{username} unregistered successfully")
            del license_plate_dict[username]

for key, value in license_plate_dict.items():
    print(f"{key} => {value}")
