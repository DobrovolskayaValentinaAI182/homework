#Практика 2
# Добровольская Валентина АИ-182
import random
from datetime import datetime
import time

def mergeSort(alist):
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0
        while i<len(lefthalf) and j<len(righthalf):
            if lefthalf[i]<righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i<len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j<len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1
    return alist

def quickSort(nums, fst, lst):
   if fst >= lst: return

   i, j = fst, lst
   pivot = nums[random.randint(fst, lst)]

   while i <= j:
       while nums[i] < pivot: i += 1
       while nums[j] > pivot: j -= 1
       if i <= j:
           nums[i], nums[j] = nums[j], nums[i]
           i, j = i + 1, j - 1
   quickSort(nums, fst, j)
   quickSort(nums, i, lst)

def heapify(arr, n, i):
    largest = i 
    l = 2 * i + 1  
    r = 2 * i + 2  

    if l < n and arr[i] < arr[l]:
        largest = l

    if r < n and arr[largest] < arr[r]:
        largest = r

    if largest != i:
        arr[i],arr[largest] = arr[largest],arr[i] 

        heapify(arr, n, largest)

def heapSort(arr):
    n = len(arr)

    for i in range(n, -1, -1):
        heapify(arr, n, i)

    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i] 
        heapify(arr, i, 0)

f = open('ai182.txt')
data = f.read()
f.close()

array = []
i = 0
while i < len(data):
    j = 0
    if data[i] == '9' and data[i+1] == ':' and data[i+2] == ' ':
        i = i + 3
        while data[i] != '}':
            array.append(data[i])
            j = j + 1
            i += 1
        break
    i+=1

resultArray = [int(i) for i in array]

# Merge sort has Duration: ~0:00:00.000942 (sometimes less)
start_time = datetime.now()
mergeSort(resultArray)
end_time = datetime.now()
print('Duration: {}'.format(end_time - start_time))

# Quick sort has Duration: ~0:00:00.000996
start_time = datetime.now()
quickSort(resultArray, 0, len(resultArray) - 1)
end_time = datetime.now()
print('Duration: {}'.format(end_time - start_time))

# Heap sort has Duration: ~0:00:00.000924
start_time = datetime.now()
heapSort(resultArray)
end_time = datetime.now()
print('Duration: {}'.format(end_time - start_time))
