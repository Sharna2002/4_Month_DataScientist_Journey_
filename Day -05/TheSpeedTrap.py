'''Create a list of 1  million numbers. Create a set (Hash table) of the same numbers. 
Check if the number -1 exist in both'''

number_list =  list(range(1,1000001))
number_set = set(range(1,1000001))

print(-1 in number_list)
print(-1 in number_set)
