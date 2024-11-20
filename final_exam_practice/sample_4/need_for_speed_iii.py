
number_of_cars = int(input())
car_dict = {}

for x in range(number_of_cars):
    car, mileage, fuel = input().split('|')
    car_dict[car] = [int(mileage), int(fuel)]

while True:
    input_string = input()
    if input_string == 'Stop':
        break
    command = input_string.split(' : ')
    command_line = command[0]
    if command_line == 'Drive':
        # "Drive : {car} : {distance} : {fuel}"
        car = command[1]
        distance = int(command[2])
        fuel = int(command[3])
        if fuel > car_dict[car][1]:
            print("Not enough fuel to make that ride")
        else:
            car_dict[car][0] += distance
            car_dict[car][1] -= fuel
            print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
            if car_dict[car][0] >= 100000:
                print(f"Time to sell the {car}!")
                del car_dict[car]
    elif command_line == 'Refuel':
        # "Refuel : {car} : {fuel}"
        car = command[1]
        fuel = int(command[2])
        if car_dict[car][1] + fuel > 75:
            litters_filled = 75 - car_dict[car][1]
            car_dict[car][1] = 75
            print(f'{car} refueled with {litters_filled} liters')
        else:
            car_dict[car][1] += fuel
            print(f'{car} refueled with {fuel} liters')
    elif command_line == 'Revert':
        car = command[1]
        kilometres = int(command[2])
        car_dict[car][0] -= kilometres
        if car_dict[car][0] < 10000:
            car_dict[car][0] = 10000
        else:
            print(f"{car} mileage decreased by {kilometres} kilometers")

for car, info in car_dict.items():
    print(f"{car} -> Mileage: {info[0]} kms, Fuel in the tank: {info[1]} lt.")