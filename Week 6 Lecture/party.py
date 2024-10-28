
class Party:

    def __init__(self):
        self.people = []

guest_list = Party()

while True:
    input_name = input()
    if input_name == "End":
        break
    guest_list.people.append(input_name)

print(f"Going: " + ", ".join(guest_list.people))
print(f"Total: {len(guest_list.people)}")