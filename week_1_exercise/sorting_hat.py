# You will be receiving names until the command "Welcome!". The length of each name determines in which house the student is going:
#     • If the name is less than 5 chars, the student is going into Gryffindor
#         ◦ Print "{name} goes to Gryffindor."
#     • If the name is exactly 5 chars, the student is going into Slytherin
#         ◦ Print "{name} goes to Slytherin."
#     • If the name is exactly 6 chars, the student is going into Ravenclaw
#         ◦ Print "{name} goes to Ravenclaw."
#     • If the name is more than 6 chars, the student is going into Hufflepuff
#         ◦ Print "{name} goes to Hufflepuff."
# While receiving names, if you receive "Voldemort", print "You must not speak of that name!" and end the program. No more sorting for today!
# If all students are sorted successfully, print "Welcome to Hogwarts."

while True:
    input_name = input()
    if input_name == "Welcome!":
        print('Welcome to Hogwarts.')
        break
    elif input_name == 'Voldemort':
        print('You must not speak of that name!')
        break
    designated_school = ''
    if len(input_name) < 5:
        designated_school = 'Gryffindor'
    elif len(input_name) == 5:
        designated_school = 'Slytherin'
    elif len(input_name) == 6:
        designated_school = 'Ravenclaw'
    else:
        designated_school = 'Hufflepuff'
    print(f'{input_name} goes to {designated_school}.')
