# QUICK SORT
import os
os.system('clear')  #operating system untuk membersihkan layar terminal
import random  #import library random

def quickSort(arr):  #fungsi quick sort yang menerima array 'arr'
    if len(arr) <= 1:  #jika panjang array kurang dari atau sama dgn 1, maka kembalikan array tersebut karena sdh dianggap terurut
        return arr
    else:
        pivot = arr[0]  #jika elemen array lebih dari satu maka tentukan sebuah pivot


        print(f"Pivot : {pivot}")
        
        less = [x for x in arr[1:] if x <= pivot]   #jika elemen lebih kecil dari pivot


        greater = [x for x in arr[1:] if x > pivot]  #jika elemen lebih besar dari pivot
    
        return quickSort(less) + [pivot] + quickSort(greater)   #kembalikan elemen lebih kecil dr pivot, pivot, elemen lebih besar dr pivot


arr = random.sample(range(20, 70), 10)  #mengimport nomor random untuk menjadi elemen dlm array

print("Array belum terurut:", arr)  #print array sblm terurut

result = quickSort(arr)  #hasil sama dengan array quick sort

print("Array sudah terurut:", result)   #print array sudah terurut
