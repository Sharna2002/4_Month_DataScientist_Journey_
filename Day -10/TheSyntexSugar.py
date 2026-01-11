# Apply the wrapper using @decorator syntax
def my_decorators(func):
    def wrapper():
        print("Before call")
        func()
        print("After call")
    return wrapper

@my_decorators
def hello():
    print("hello world")

hello()