x = int(input("Enter a number of repetitions"))
def repeat_decorator(num_repetitions):
    def decorator_func(func):
        def wrapper_func():
            for _ in range(num_repetitions):
                func()
        return wrapper_func
    return decorator_func

@repeat_decorator(x)
def hello():
    print('Hello')

hello()
