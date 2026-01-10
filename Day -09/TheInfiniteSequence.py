# Write a while True generator that produces fibonacci numbers forever.
def fibonacchi():
    a,b = 0,1
    while True:
        yield a
        a,b = b, a+b
    
ans = fibonacchi()

for _ in range(10):
    print(next(ans))