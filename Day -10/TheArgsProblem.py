# Try to decorate a function that takes arguments add(a,b) with a wrapper that takes none
def decorator(original_function):
    def wrapper(*args,**kwargs):
        print("Answer is: ")

        result = original_function(*args,**kwargs)
        return result
    return wrapper

@decorator
def add(a,b):
    return a + b

print(add(3,5))
