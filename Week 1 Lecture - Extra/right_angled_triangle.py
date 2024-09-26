# Develop a Python script that generates a right-angled triangle pattern. The script should prompt the user to specify the number of rows.
# Here's a sample output for a user input of 5:
# *
# **
# ***
# ****
# *****

input_rows = int(input())

for i in range(1, input_rows + 1):
    print(i * "*")