# Write a generator that yield values from two different sub_generators using yield from

def gen1():
    yield 1
    yield 2
    
def gen2():
    yield 3
    yield 4

def gen():
    yield from gen1()
    yield from gen2()

for i in gen():
    print(i)