# Compare sys.getsizeof() of a List Comprehension vs a Generator Expression for 1 million numbers.
import sys 

my_list = [x for x in range(1000000)]
My_generator = (x for x in range(1000000))

print(f"{sys.getsizeof(my_list)} bytes")
print(f"{sys.getsizeof(My_generator) } bytes")
