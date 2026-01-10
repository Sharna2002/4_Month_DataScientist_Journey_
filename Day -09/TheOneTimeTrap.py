# create a generator g. loop through it once. Try to loop through it again.
def g():
    yield 1 
    yield 2
    yield 3

my_gen = g()

print("First loop :")
for i in my_gen:
    print(i)

print("Second loop :")
for i in my_gen:
    print(i)


