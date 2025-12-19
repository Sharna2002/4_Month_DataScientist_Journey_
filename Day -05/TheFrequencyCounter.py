# Input a string "banana". Create a dictionary that counts the frequency of each character.
#  (e.g.,{"b":1,"a":3,"n":2}

string = "banana"

dict = {}

for ch in string:
    if ch not in dict:
        dict[ch] = 1
    else:
        dict[ch] += 1
    
print(dict)