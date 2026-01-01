# Convert this list to a set. Check for -5 again.

def checkNumber(set_value,target):
    #hash_value = calculate_hash(target)
    ...


def main():
    list_value = list(range(1,1000001)) 
    set_value = set(list_value)
    target = -5
    print(checkNumber(set_value,target))

main()