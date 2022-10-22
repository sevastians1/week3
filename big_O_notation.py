def largest(array, value):
  for item in array:
    if item > value:
      return False
  return True 
  ##O(n)
def info_dump(customers):
  
  print('Customer Names:')
  for customer in customers: 
    print(customer['name'])
  
  print('Customer Locations:')
  for customer in customers: 
    print(customer['country'])
##O(2n)-->O(n)
def first_element_is_red(array):
  return array[0] == 'red' 
##O(1)
def duplicates(array):
  for index1, item1 in enumerate(array):
    for index2, item2 in enumerate(array):
      if index1 == index2:
        continue
      if item1 == item2:
        return True
  return False
##O(n^2)
# words = ['chocolate', 'coconut', 'rainbow']
# endings = ['cookie', 'pie', 'waffle']

# for word in words:
#   for ending in endings:
#     print(word + ending)
#O(1)
numbers = [2, 1,3,6, 2, 4, 11, 5, 7,9,10]
def print_array(array):
  for item in array:
    print(item)
##O(n)
# this is insertion sort
def insertionSort(arr): 
  for i in range(1, len(arr)): 
    key = arr[i] 
    j = i-1
    print(i, key, "upper")
    while j >=0 and key < arr[j] : 
      arr[j+1] = arr[j] 
      print("lower")
      j -= 1
    arr[j+1] = key 
  return arr
#j is index minus 1, 
##O(n^2)

for i in range(len(numbers)):
  min_idx = i
  print(min_idx, "i")
  for j in range(i+1, len(numbers)):
    print(j, "j", min_idx, "min_idx", numbers[j])
    if numbers[min_idx] > numbers[j]:
        min_idx = j

  numbers[i], numbers[min_idx] = numbers[min_idx], numbers[i]
print(numbers)
  #O(n^2)