dwarf_data = {}
hat_color_count = {}

while True:
    input_string = input()
    if input_string == "Once upon a time":
        break

    dwarf_name, dwarf_hat_color, dwarf_physics = input_string.split(" <:> ")
    dwarf_physics = int(dwarf_physics)

    key = (dwarf_name, dwarf_hat_color)

    if key not in dwarf_data or dwarf_data[key] < dwarf_physics:
        dwarf_data[key] = dwarf_physics

for (name, color) in dwarf_data.keys():
    if color not in hat_color_count:
        hat_color_count[color] = 0
    hat_color_count[color] += 1

final_dwarfs = [(color, name, physics) for (name, color), physics in dwarf_data.items()]

final_dwarfs = sorted(final_dwarfs, key=lambda x: (-x[2], -hat_color_count[x[0]]))

for color, name, physics in final_dwarfs:
    print(f"({color}) {name} <-> {physics}")
