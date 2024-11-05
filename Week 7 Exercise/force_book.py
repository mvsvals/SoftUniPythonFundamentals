
force_dict = {}

while True:
    input_string = input()

    if input_string == "Lumpawaroo":
        break

    if " | " in input_string:
        force_side, force_user = input_string.split(' | ')
        is_existing_user = False

        for side_members in force_dict.values():
            if force_user in side_members:
                is_existing_user = True

        if not is_existing_user:
            if force_side not in force_dict.keys():
                force_dict[force_side] = []
            force_dict[force_side].append(force_user)

    elif ' -> ' in input_string:
        force_user, force_side = input_string.split(' -> ')
        is_existing_user = False
        existing_user_side = ''

        if force_side not in force_dict.keys():
            force_dict[force_side] = []

        for side, users in force_dict.items():
            if force_user in users:
                is_existing_user = True
                existing_user_side = side

        if is_existing_user:
            force_dict[existing_user_side].remove(force_user)
        force_dict[force_side].append(force_user)

        print(f"{force_user} joins the {force_side} side!")


for side, members in force_dict.items():
    if len(members) > 0:
        print(f"Side: {side}, Members: {len(members)}")
        for member in force_dict[side]:
            print("! " + member)


