# Create a @timer decorator that prints execution time using time.time()
import time

def timer(func):
    def wrapper():
        start = time.time()
        func()
        print(time.time() - start)
    return wrapper

@timer
def clock():
    time.sleep(1)

clock()