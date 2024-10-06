# Write a function that receives a string and a counter n.
# The function should return a new string – the result of repeating the old string n times.
# Print the result of the function. Try using lambda.

input_string = input()
counter = int(input())

new_string = lambda string, times: string * times
print(new_string(input_string, counter))