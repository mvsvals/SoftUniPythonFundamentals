# You have a water tank with a capacity of 255 liters. On the first line, you will receive n – the number of lines, which will follow.
# On the following n lines, you will receive liters of water (integers), which you should pour into your tank.
# If the capacity is not enough, print "Insufficient capacity!" and continue reading the next line. On the last line, print the liters in the tank.

tank_capacity = 255
litres_into_tank = 0

input_lines = int(input())

for i in range(input_lines):
    pour_into_tank = int(input())
    if pour_into_tank + litres_into_tank > tank_capacity:
        print('Insufficient capacity!')
        continue
    else:
        litres_into_tank += pour_into_tank

print(litres_into_tank)