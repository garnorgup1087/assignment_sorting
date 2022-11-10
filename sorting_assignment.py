import pandas as pd
comp_selection_sort=0
comp_bubble_sort=0
swap_selection_sort=0
swap_bubble_sort=0
# Selection sort in Python
def selectionSort(array, size):
    global comp_bubble_sort,comp_selection_sort,swap_bubble_sort,swap_selection_sort
    for step in range(size):
        min_idx = step
        for i in range(step + 1, size):
            comp_selection_sort=comp_selection_sort+1
            if array[i] < array[min_idx]:
                min_idx = i
        (array[step], array[min_idx]) = (array[min_idx], array[step])
        swap_selection_sort=swap_selection_sort+1
    return comp_selection_sort,swap_selection_sort

# Bubble sort in Python

def bubbleSort(array):
  global comp_bubble_sort,comp_selection_sort,swap_bubble_sort,swap_selection_sort
  for i in range(len(array)):
    for j in range(0, len(array) - i - 1):
      # compare two adjacent elements
      comp_bubble_sort=comp_bubble_sort+1
      if array[j] > array[j + 1]:
        # swapping elements if elements
        temp = array[j]
        array[j] = array[j+1]
        array[j+1] = temp
        swap_bubble_sort=swap_bubble_sort+1
  return comp_bubble_sort,swap_bubble_sort

data1 = [-2, 45, 0, 11, -9,10,89,56,78,345,7643,90,-97,-97,-0,0,78,78,6,543,78,654]
data2 = [-2, 45, 0, 11, -9,10,89,56,78,345,7643,90,-97,-97,-0,0,78,78,6,543,78,654]
size1 = len(data1)
selectionSort(data1, size1)
bubbleSort(data2)
print('Sorted Array in Ascending Order by Selection sort:')
print(data1)
print('Sorted Array in Ascending Order by Bubble sort:')
print(data2)
print('Number of comparisons in selection sort: ')
print(comp_selection_sort)
print('Number of comparisons in bubble sort: ')
print(comp_bubble_sort)
print('Number of swaps in selection sort: ')
print(swap_selection_sort)
print('Number of swaps in bubble sort: ')
print(swap_bubble_sort)


#both selection sort and bubble sort are inplace

#bonus
import time
start_time=time.time()
for i in range(0,100000):
    selectionSort(data1, size1)
end_time=time.time()
tim=end_time-start_time
print('time taken by selection sort')
print(tim)


import time
start_time=time.time()
for i in range(0,100000):
     bubbleSort(data2)
end_time=time.time()
tim1=end_time-start_time
print('time taken by bubble sort')
print(tim1)