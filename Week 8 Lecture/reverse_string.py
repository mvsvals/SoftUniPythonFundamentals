while True:
    input_text = input()

    if input_text == 'end':
        break

    print(f'{input_text} = {input_text[::-1]}')