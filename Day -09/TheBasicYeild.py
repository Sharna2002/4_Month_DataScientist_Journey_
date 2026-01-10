# Write a function gen() that yeilds 1, then 2, then 3. Loop through it.
def gen():
    yield 1
    yield 2
    yield 3

for i in gen():
    print(i)

