# Slice a massive list data[0:5000].
def slice_list(source,k):
    new_list = allocate(k)

    for i in range(k):
        new_list[i] = source[i]

    return new_list
def allocate(k):
    return [None]*k
def main():
    my_list = list(range(5000))
    print(slice_list(my_list,50))
main()
