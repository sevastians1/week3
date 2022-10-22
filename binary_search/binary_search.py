import random 
def binary_search(index, values):
    values.sort()
    low=0
    high=len(values)-1
    while low<=high:
        middle=low+(high-low)//2
        # print(middle, "middle", values[middle])
        # print(values[middle], index)
        if values[middle]==index:
            return middle
        elif values[middle]<index:
            low=middle+1
        elif values[middle]>index:
            high=middle-1
    return -1


# get length of the array 
# find the middle index of the array
# compare target value with value at middle index 
# if value at middle index equals target value, return index - BASE CASE
# if value at middle index less than target value, call function recursively with left half of array - RECURSIVE CASE 
# if value at middle index greater than target value, call function recursively on right half of array - RECURSIVE CASE

# values = random.sample(list(range(1,10000)), 1000)

# test_array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# print(binary_search(1, test_array))
# print(binary_search(2, test_array) == 2)
# print(binary_search(3, test_array))
# print(binary_search(4, test_array))
# print(binary_search(2, test_array))
# print(binary_search(8, test_array))