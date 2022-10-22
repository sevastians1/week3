def binary_search(target_value, test_array):
    array_length = len(test_array)
    if array_length == 0: # Base case 
        return -1
    else:
        middle_index = array_length // 2
        # print("middle_index: ", middle_index, test_array)
        if test_array[middle_index] == target_value:
            # print("returning: ", middle_index)
            return middle_index
        elif target_value < test_array[middle_index]:
            return binary_search(target_value, test_array[:middle_index])
        elif target_value > test_array[middle_index]:
            return middle_index+ binary_search(target_value, test_array[middle_index:]) 


test_array = [0,1,2,3,4,5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15] 


print(binary_search(1, test_array) == 1)
print(binary_search(2, test_array) == 2)
print(binary_search(3, test_array) == 3)
print(binary_search(4, test_array) == 4)
print(binary_search(5, test_array) == 5)
print(binary_search(6, test_array) == 6)
print(binary_search(7, test_array) == 7)
print(binary_search(8, test_array) == 8)
print(binary_search(9, test_array) == 9)
print(binary_search(10, test_array) == 10)
print(binary_search(11, test_array) == 11)
print(binary_search(12, test_array) == 12)
print(binary_search(13, test_array)  == 13)
print(binary_search(14, test_array) == 14)
print(binary_search(15, test_array) == 15)
# receiving an array of 1000 unique values 
    # if array is empty return -1 - BASE CASE 

# get length of the array 
# find the middle index of the array
# compare target value with value at middle index 
# if value at middle index equals target value, return index - BASE CASE
# if value at middle index less than target value, call function recursively with left half of array - RECURSIVE CASE 
# if value at middle index greater than target value, call function recursively on right half of array - RECURSIVE CASE

# two parameters: target value, test array 