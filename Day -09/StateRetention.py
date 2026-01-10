# Write a generator that calculate a "Running average" 
def accumulator():
    total = 0
    count = 0
    while True:
        val = yield total / count if count else 0
        total = val + total
        count += 1

avg = accumulator()

next(avg)
print(avg.send(10))
print(avg.send(20))


