# Compare list.append(x) vs list.insert(0,x).
def insert_at_zero(my_list, new_value):
    n = len(my_list)

    my_list.append(None)

    for i in range(n, 0, -1):
        my_list[i] = my_list[i - 1]

    my_list[0] = new_value

def main():
    my_list = [10, 20, 30]
    insert_at_zero(my_list, 5)
    print(my_list)
main()

""" In list.insert(0,x) n elements need to shift n position so the time complexity is O(N).It executes slower
    In list.append(x)  its free up to the next empty slot. It's doesn't requiere any shifting. 
    Time complexity is O(1). It executes faster.   
 """