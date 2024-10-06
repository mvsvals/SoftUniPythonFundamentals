
input_grade = float(input())

def grading(grade):
    if grade >= 5.50:
        return 'Excellent'
    elif grade >= 4.50:
        return 'Very Good'
    elif grade >= 3.50:
        return 'Good'
    elif grade >= 3.00:
        return 'Poor'
    else:
        return 'Fail'

print(grading(input_grade))
