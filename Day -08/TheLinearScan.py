# Create a list of 10 milion numbers. Check -5 is in the list. 

def checkNumber(lst,target):
    index = 0
    length = len(lst)
    while index < length:
        if lst[index] == target:
            return True
        index += 1
        
    return False

def main():
    lst = list(range(1,1000001)) 
    target = -5
    print(checkNumber(lst,target))

main()
