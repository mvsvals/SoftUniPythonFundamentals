single_lift_capacity = 4

people_waiting = int(input())
lift_status = [int(wagon) for wagon in input().split()]

for i in range(len(lift_status)):
    while lift_status[i] < single_lift_capacity and people_waiting > 0:
        lift_status[i] += 1
        people_waiting -= 1

final_lift_status = " ".join(map(str, lift_status))

if people_waiting == 0 and sum(lift_status) < len(lift_status) * single_lift_capacity:
    print(f"The lift has empty spots!")
elif people_waiting > 0:
    print(f"There isn't enough space! {people_waiting} people in a queue!")

print(final_lift_status)