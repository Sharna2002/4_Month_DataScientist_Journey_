 # Write a script that asks the user for a password repeatedly.
 # It must run forever until the user types "stop".

while True:
    passkey = input("Enter passward: ")
    if passkey == "stop":
        break
    
    