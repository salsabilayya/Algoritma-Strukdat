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
