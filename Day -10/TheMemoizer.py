# Write a @cache decorator that stores results of extensive function calls in a dictionary.

def cache_decorator(func):
    store = {}
    def wrapper(n):
        if n in store:
            return store[n]
        store[n] = func(n)
        return store[n]
    return wrapper

@cache_decorator

def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)
print(fib(10))
