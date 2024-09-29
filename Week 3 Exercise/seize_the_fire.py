fires_cells_input = input().split("#")
water_amount = int(input())
total_effort = 0
total_cells_put_out = []

for element in fires_cells_input:
    element_separated_list = element.split(" = ")
    if water_amount > int(element_separated_list[1]) and ((element_separated_list[0] == 'High' and 81 <= int(element_separated_list[1]) <= 125) or \
        (element_separated_list[0] == 'Medium' and 51 <= int(element_separated_list[1]) <= 80) or \
        (element_separated_list[0] == 'Low' and 1 <= int(element_separated_list[1]) <= 50)):
            water_amount -= int(element_separated_list[1])
            total_effort += 0.25 * int(element_separated_list[1])
            total_cells_put_out.append(int(element_separated_list[1]))
    else:
        continue

print("Cells:")
print(*[f' - {item}' for item in total_cells_put_out], sep='\n')
print(f'Effort: {total_effort:.2f}')
print(f'Total Fire: {sum(total_cells_put_out)}')


