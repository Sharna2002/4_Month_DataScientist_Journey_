# Create a list of numbers from 1 to 10. Generate a new list containing the squares of only even numbers.

data = [x**2 for x in range(1,11) if x % 2 == 0]

print(data)