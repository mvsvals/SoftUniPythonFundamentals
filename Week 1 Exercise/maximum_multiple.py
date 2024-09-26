# On the first line, you will be given a positive number, which will serve as a divisor.
# On the second line, you will receive a positive number that will be the boundary. You should find the largest integer N, that is:
#     • divisible by the given divisor
#     • less than or equal to the given bound
#     • greater than 0
# Note: it is guaranteed that N is found.

divisor_number = int(input())
boundary_number = int(input())

for i in range(boundary_number, divisor_number - 1, -1):
    if i % divisor_number == 0 and i <= boundary_number:
        print(i)
        break


