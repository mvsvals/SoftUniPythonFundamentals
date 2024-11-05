# Write a program that keeps the information about companies and their employees.
# You will be receiving company names and an employees' id until you receive the command "End" command.
# Add each employee to the given company. Keep in mind that a company cannot have two employees with the same id.
# Print the company name and each employee's id in the following format:
# "{company_name}
# -- {id1}
# -- {id2}
# …
# -- {idN}"
# Input / Constraints
#     • Until you receive the "End" command, you will be receiving input in the format:
# "{company_name} -> {employee_id}".
#     • The input always will be valid.

employee_dict = {}

while True:
    input_string = input()
    if input_string == 'End':
        break
    company_name, employee_id = input_string.split(' -> ')
    if company_name not in employee_dict.keys():
        employee_dict[company_name] = [employee_id]
    else:
        if employee_id not in employee_dict[company_name]:
            employee_dict[company_name].append(employee_id)

for company in employee_dict.keys():
    print(company)
    for employee in employee_dict[company]:
        print(f'-- {employee}')