# You will receive 3 strings on separate lines, representing the tail, the body, and the head of an animal in that order.
# Your task is to re-arrange the elements in a list so that the animal looks normal again:
#     • On the first position is the head;
#     • On the second position is the body;
#     • On the last one is the tail.


arranged_list = []

for _ in range(3):
    data_input = input()
    arranged_list.append(data_input)

arranged_list[0], arranged_list[2] = arranged_list[2], arranged_list[0]

print(arranged_list)


