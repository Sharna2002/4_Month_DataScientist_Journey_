# Create two generators: one squares numbers, the other filters evens. Chain them: filter(square(nums))

def square(nums):
    for i in nums:
        yield i*i

def even(nums):
    for i in nums:
        if i % 2 == 0:
            yield i 

nums = range(1,11)
pipeline = even(square(nums))

for number in pipeline:
    print(number)
