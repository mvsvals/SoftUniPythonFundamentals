
number_of_cars = int(input())
cars_dict = {}

for x in range(number_of_cars):
    car, mileage, fuel = input().split('|')
    cars_dict[car] = {'mileage': int(mileage), 'fuel': int(fuel)}

while True:
    input_string = input()
    if input_string == 'Stop':
        break
    command = input_string.split(' : ')
    if command[0] == 'Drive':
        car, distance, fuel = command[1], int(command[2]), int(command[3])
        if fuel > cars_dict[car]['fuel']:
            print("Not enough fuel to make that ride")
        else:
            cars_dict[car]['fuel'] -= fuel
            cars_dict[car]['mileage'] += distance
            print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
            if cars_dict[car]['mileage'] > 100000:
                print(f"Time to sell the {car}!")
                del cars_dict[car]
    elif command[0] == 'Refuel':
        car, fuel = command[1], int(command[2])
        refueled_amount = 0
        if fuel + cars_dict[car]['fuel'] > 75:
            refueled_amount = 75 - cars_dict[car]['fuel']
            cars_dict[car]['fuel'] = 75
        else:
            refueled_amount = fuel
            cars_dict[car]['fuel'] += fuel
        print(f"{car} refueled with {refueled_amount} liters")
    elif command[0] == 'Revert':
        car, kilometres = command[1], int(command[2])
        cars_dict[car]['mileage'] -= kilometres
        if cars_dict[car]['mileage'] < 10000:
            cars_dict[car]['mileage'] = 10000
        else:
            print(f"{car} mileage decreased by {kilometres} kilometers")

for car, car_data in cars_dict.items():
    print(f"{car} -> Mileage: {car_data['mileage']} kms, Fuel in the tank: {car_data['fuel']} lt.")