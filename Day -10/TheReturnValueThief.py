# Write a decorator that forgets to return func(*args). Print the result of the decorated function.
def broken_wrapper(func):
    def wrapper():
        func()
    return wrapper

@broken_wrapper
def working_wrapper():
    return 10

print(working_wrapper())
