# Measure the time to create a dict from a list vs searching it.
import time
def build_dict_from_list(my_list):
    new_dict = allocate_memory(my_list)

    for item in my_list:
        hash_val = calculate_hash(item,len(new_dict))
        slot = find_empty_slot(hash_val)
        new_dict[slot] = item
    return new_dict

def allocate_memory(my_list):
    return [None]*len(my_list)
def calculate_hash(item,size):
    return hash(item) % size
def find_empty_slot(hash_val):
    return hash_val

def main():
    my_list = list(range(1,100))
    start_time = time.perf_counter()
    hash_table = build_dict_from_list(my_list)
    end_time = time.perf_counter()
    print("Time to create dict: ", end_time - start_time)

    start_time = time.time()
    end_time = time.time()
    print("Time to search in list:", end_time - start_time)

main()

