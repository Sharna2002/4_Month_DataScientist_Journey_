# create a variable x = 0. Try to print 100 / x. Catch the specific errors that occurs.

x = 0

try:
    print(100/x)
except:
    print("Skipping bad row")