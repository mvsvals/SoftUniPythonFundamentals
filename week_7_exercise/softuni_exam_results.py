
exam_results = {}
language_submissions = {}

while True:
    input_string = input()

    if input_string == 'exam finished':
        break

    if 'banned' in input_string:
        banned_user = input_string.split('-')[0]
        del exam_results[banned_user]
    else:
        submission = input_string.split('-')
        username, language, points = submission[0], submission[1], int(submission[2])
        if username not in exam_results.keys():
            exam_results[username] = 0
        if language not in language_submissions.keys():
            language_submissions[language] = 0
        language_submissions[language] += 1
        if points > exam_results[username]:
            exam_results[username] = points

print('Results:')
for student, points in exam_results.items():
    print(f'{student} | {points}')

print('Submissions:')
for language, submissions in language_submissions.items():
    print(f'{language} - {submissions}')


