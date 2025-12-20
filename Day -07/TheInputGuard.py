# write a script that asks user for their age. If they type text (e.g,"twenty") 
# print "Numbers only" instead of crashing

try:
    age = int(input("Enter your age: "))
    print(f"Age is {age}")
    
except ValueError:
    print("Numbers only")