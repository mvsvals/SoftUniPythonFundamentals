
fires_cells_input = input().split("#")
water_amount = int(input())

total_effort = 0
total_cells_put_out = []

for element in fires_cells_input:
    element_separated_list = element.split(" = ")
    fire_type = element_separated_list[0]
    fire_value = int(element_separated_list[1])

    if (fire_type == 'High' and 81 <= fire_value <= 125) or \
       (fire_type == 'Medium' and 51 <= fire_value <= 80) or \
       (fire_type == 'Low' and 1 <= fire_value <= 50):
        # Check if there is enough water to put out the fire
        if water_amount >= fire_value:
            water_amount -= fire_value
            total_effort += 0.25 * fire_value
            total_cells_put_out.append(fire_value)

print("Cells:")
for cell in total_cells_put_out:
    print(f" - {cell}")

print(f"Effort: {total_effort:.2f}")
print(f"Total Fire: {sum(total_cells_put_out)}")
