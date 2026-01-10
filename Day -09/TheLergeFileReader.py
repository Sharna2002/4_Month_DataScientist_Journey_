# Write a generator to read a "fake" 100GB file line-by-line

def fake_file():
    for i in range(5):
        yield f"line{i}"

for line in fake_file():
    print(line)
