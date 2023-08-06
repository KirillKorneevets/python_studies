from datetime import datetime


def new_decorator(function_to_decorate):

    def wrapper(*args, **kwargs):
        start_time = datetime.now()
        result = function_to_decorate(*args, **kwargs)
        print(result)
        end_time = datetime.now()
        execution_time = start_time - end_time
        print(execution_time)
        return result

    return wrapper


a = [1,2,3,4,5]
@new_decorator
def sum_list(numbers):
    return sum(numbers)
sum_list(a)



@new_decorator
def f(**kwargs):
    for k,v in kwargs.items():
        print(k,v)
f(c = 10, g = 20, p = 30)
