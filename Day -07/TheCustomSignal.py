# Ask the user for a number. If the number is negative manually trigger a error 
# using raise ValueError("No negatives")

try:
    num = int(input("Enter a number: "))

    if num < 0:
        raise ValueError("No negatives")
    
    print(f"Number is {num}")
    
except ValueError as error:
    print("Error exist: ",error)