class Calculator():

    @classmethod
    def sum(cls,a,b):
        return a+b

    @classmethod
    def subtrack(cls,a,b):
        return a-b
    
    @classmethod
    def multiply(cls,a,b):
        return a*b
    
    @classmethod
    def divide(cls,a,b):
        if b == 0:
            return a/b
    
OPERATORS_NUM = {"+":Calculator.sum,
     "-":Calculator.subtrack,
     "*":Calculator.multiply,
     "/":Calculator.divide
     }

while True:
    try:
        x = int(input("Введите первое число: "))
        y = int(input("Введите второе число: "))
        action = (input("Выберите действие (+,-,*,/): "))
    
        result = OPERATORS_NUM[action](x,y)
        print(result)
    except ValueError as e:
            print (f"Вы ввели некорректное значение: {e}")
    except ZeroDivisionError as e:
            print(f"Деление на ноль невозможно: {e}")
    except TypeError as e:
            print(f"Некорректный тип данных: {e}")
    except KeyError as e:
            print(f"Некорректный оператор: {e}")
