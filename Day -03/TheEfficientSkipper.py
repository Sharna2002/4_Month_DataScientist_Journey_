#Loop through numbers 1 to 10. Print them, BUT if the number is 5, skip it and do not print anything.

for i in range(1,10+1):
    if i == 5:
        continue
    else:
        print(i)