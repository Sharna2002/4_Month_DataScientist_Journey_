# Write a function wrapper(func) that runs code before/after func. Apply it manually: new_func = wrapper(old_func)

def my_decorators(func):
    def wrapper():
        print("Before call")
        func()
        print("After call")
    return wrapper
def hello():
    print("hello world")

new_func = my_decorators(hello)

new_func()