# You will receive two lines of input:
#     • a list of employees' happiness as a string of numbers separated by a single space
#     • a happiness improvement factor (single number).
# Your task is to find out if the employees are generally happy in their office.
# First, multiply each employee's happiness by the factor.
# Then, print one of the following lines:
#     • If half or more of the employees have happiness greater than or equal to the average:
# "Score: {happy_count}/{total_count}. Employees are happy!"
#     • Otherwise:
# "Score: {happy_count}/{total_count}. Employees are not happy!"


employee_happiness = input().split()
happiness_improvement_factor = int(input())

employee_happiness = list(map(lambda x: int(x) * happiness_improvement_factor, employee_happiness))
filtered_employee_data = list(map(lambda x: x > sum(employee_happiness) / len(employee_happiness), employee_happiness))

if filtered_employee_data.count(True) >= len(employee_happiness) / 2:
    print(f"Score: {filtered_employee_data.count(True)}/{len(employee_happiness)}. Employees are happy!")
else:
    print(f"Score: {filtered_employee_data.count(True)}/{len(employee_happiness)}. Employees are not happy!")



