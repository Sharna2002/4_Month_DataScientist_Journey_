# compare list.pop() vs list.pop(0).
def pop_from_start(my_list):
    target = my_list[0]
    n = len(my_list)

    for i in range(0,n-1):
        my_list[i] = my_list[i+1]

    n = len(my_list)
    return target


def main():
    my_list = [10, 20, 30]
    print(pop_from_start(my_list))

main()

''' list.pop() follows the stack(last in first out). This function removes the last element of 
    the list without shifting any element. Which complexity is O(1). Faster execution.
    list.pop(0) follows the queue(first in first out). This function removes the first element of 
    the list though shifting the next elements in the previous position. Which complexity is O(N). 
    Slower execution.
'''