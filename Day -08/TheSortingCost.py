# Sort a random list
def merge_sort(my_list):
    sz = len(my_list)
    if sz <= 1:
        return my_list
    else:
        mid = sz // 2
        left = merge_sort(my_list[0:mid])
        right = merge_sort(my_list[mid:])
        return merge(left,right)

def merge(left,right):
    ans = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            ans.append(left[i])
            i += 1
        else:
            ans.append(right[j])
            j += 1
    ans.extend(left[i:])
    ans.extend(right[j:])
    return ans
        
            
def main():
    my_list = [5,8,6,1]
    print(merge_sort(my_list))
    
main()