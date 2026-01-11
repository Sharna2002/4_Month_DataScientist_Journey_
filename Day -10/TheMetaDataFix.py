# print func.__name__ of a decorated function.
def decorator(func):
    def wrapper():
        pass
    return wrapper

@decorator
def show():
    pass
print(show.__name__)