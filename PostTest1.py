# import random

# def merge_sort(arr):
#     if len(arr) <= 1:
#         return arr
    
#     mid = len(arr) // 2
#     left = arr[:mid]
#     right = arr[mid:]

#     left = merge_sort(left)
#     right = merge_sort(right)

#     return merge(left, right)

# def merge(left, right):
#     result = []
#     i = 0
#     j = 0

#     while i < len(left) and j < len(right):
#         if left[i] < right[j]:
#             result.append(left[i])
#             i += 1
#         else:
#             result.append(right[j])
#             j += 1
#     return result

# arr = [28, 22, 3, 31, 56]
# print("Array yang belum terurut:", arr)

# print()

# result = merge_sort(arr)
# print("Array yang sudah terurut:", result)

# QUICK SORT
import os
os.system('clear')
import random

def quickSort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0] 

        print(f"Pivot : {pivot}")
        
        less = [x for x in arr[1:] if x <= pivot]

        greater = [x for x in arr[1:] if x > pivot]
    
        return quickSort(less) + [pivot] + quickSort(greater)


arr = random.sample(range(20, 70), 10)

print("Array belum terurut:", arr)

result = quickSort(arr)

print("Array sudah terurut:", result)