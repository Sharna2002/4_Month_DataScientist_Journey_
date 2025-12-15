# Ask the user for a number N(ex: 5). Calculate the sum of all numbers from 1 to N (1 + 2 + 3 + 4 + 5).

num = int(input("Enter a number: "))
sum = 0
i = 1
for i in range(num+1):
    sum +=  i

print(f"The sum is: {sum}")