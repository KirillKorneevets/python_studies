def numbers(input_string):
    if input_string.lstrip('-').replace('.', '', 1).isdigit():
        if '.' in input_string:
            modified_number = float(input_string)
            if input_string.startswith('-'):
                return f'Вы ввели отрицательное дробное число: {modified_number}'
            else:
                return f'Вы ввели положительное дробное число: {modified_number}'
        else:
            modified_number = int(input_string)
            if input_string.startswith('-'):
                return f'Вы ввели отрицательное целое число: {modified_number}'
            else:
                return f'Вы ввели положительное целое число: {modified_number}'
    else:
        return f"Вы ввели некорректное число: {input_string}"


print(numbers("-6.7"))
print(numbers("5"))
print(numbers("5.4r"))
print(numbers("-.777"))          


