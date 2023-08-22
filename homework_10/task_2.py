class Calculator:
    @classmethod
    def sum(cls, a, b):
        return a + b

    @classmethod
    def subtract(cls, a, b):
        return a - b

    @classmethod
    def multiply(cls, a, b):
        return a * b

    @classmethod
    def divide(cls, a, b):
        if b == 0:
            raise ZeroDivisionError("Деление на ноль невозможно")
        return a / b


OPERATORS = {
    "+": "sum",
    "-": "subtract",
    "*": "multiply",
    "/": "divide"
}

while True:
    try:
        x = int(input("Введите первое число: "))
        y = int(input("Введите второе число: "))
        action = input("Выберите действие (+, -, *, /): ")

        if action in OPERATORS:
            method_name = OPERATORS[action]
            method = getattr(Calculator, method_name)
            result = method(Calculator, x, y)
            print(result)
        else:
            print("Некорректный оператор")
    except ValueError as e:
        print(f"Вы ввели некорректное значение: {e}")
    except ZeroDivisionError as e:
        print(f"Деление на ноль невозможно: {e}")
    except TypeError as e:
        print(f"Некорректный тип данных: {e}")
