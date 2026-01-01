# Find dublicates between two lists using nested for loops.
def find_duplicates(list_a,list_b):
    matches = []
    for item_a in list_a:
        for item_b in list_b:
            if item_a == item_b:
                matches.append(item_a)
    
    return matches
def main():
    list_a = list(range(0,10000))
    list_b = list(range(9990,19550))
    print(find_duplicates(list_a,list_b))

main()