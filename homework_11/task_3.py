import re


email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

def filtration_email(n):
    email = re.findall(email_pattern, n)
    if email:
        return 'Email адресс введен верно'
    else:
        return 'Некорректный email адресс'

n = (input('Введите ваш Email: '))

print(filtration_email(n))


