* The spped trap -<br>
    number_list =  list(range(1,1000001)) <b> # This line indicate a list.</b> <br>
    number_set = set(range(1,1000001))  <b> #  This line indicates a set.</b> <br>

    print(-1 in number_list) <br>
    print(-1 in number_set)<br>
    For searching -1 in a list use the time complexity of O(N), beacuse internally it follows the loop function to searching and search iteratively. In the otherhand set/ dict is searching the value of the key  -1, mainly the hash value of the key. Which time complexity is O(1). So, set is faster than list.
  
