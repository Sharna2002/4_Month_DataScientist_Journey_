# Use gen.send(value) to inject data into a running generator  
def coroutines():
    while True:
        data_received = yield
        print(data_received)

gen = coroutines()
next(gen)
gen.send("hi")