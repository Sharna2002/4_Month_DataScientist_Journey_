# Manually call next(gen) until it crashes.
def gen():
    yield 1
    yield 2
    yield 3

my_generator = gen()

print(next(my_generator))
print(next(my_generator))
print(next(my_generator))
print(next(my_generator))