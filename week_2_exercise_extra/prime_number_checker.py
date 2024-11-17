# Write a program to check if a number is prime.
# A prime number is a natural number greater than 1, not a product of two smaller natural numbers. For example, the only ways of writing 5 as a product, 1 × 5 or 5 × 1, involve 5 itself.
# The input comes as an integer number.
# The output should be True if the number is prime and False otherwise.

input_number = int(input())
is_prime_number = True

for i in range(2, input_number):
    if input_number % i == 0:
        is_prime_number = False
        break

print(is_prime_number)