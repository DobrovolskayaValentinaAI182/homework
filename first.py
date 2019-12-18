from random import randrange
import time
from datetime import datetime

#buble
my_list = [ randrange(0, 15) for i in range(10) ]

max_list = len( my_list )

i = 0
while i < max_list:

    j = 0
    while j < max_list-i-1:

        if my_list[ j ] > my_list[ j + 1 ]:

            my_list[ j ], my_list[ j + 1] = my_list[ j + 1], my_list[ j ]
        j+=1
    i += 1

print( my_list )



from datetime import datetime
start_time = datetime.now()
# do your work here
end_time = datetime.now()
print('Duration: {}'.format(end_time - start_time))
# Добровольская Валентина
# АИ-182
# Практика 1

def bubbleSort(array):
    for i in range (len(array)):
        for j in range (len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array

def insertionSort(array):
    for i in range (1, len(array)):
        x = array[i]
        j = i
        while j > 0 and array[j - 1] > x:
            array[j] = array[j - 1]
            j = j - 1
        array[j] = x
    return array

def selectionSort(array):
    for i in range (len(array) - 1):
        minIndex = i
        for j in range (i + 1, len(array)):
            if array[j] < array[minIndex]:
                minIndex = j
        if minIndex != i:
            array[i], array[minIndex] = array[minIndex], array[i]
    return array

arrayForBubbleSort = [ 659, 83, 250, 390, 909, 23, 769, 238, 323, 589, 527, 497, 130, 428, 515 ]
print(" Bubble sort: ", bubbleSort(arrayForBubbleSort), "\n")

arrayForInsertionSort = [ 484, 310, 976, 364, 244, 715, 353, 871, 994, 4, 419, 415, 384, 760, 97 ] 
print(" Insertion sort: ", insertionSort(arrayForInsertionSort), "\n")

arrayForSelectionSort = [ 809, 52, 503, 139, 34, 960, 237, 135, 865, 654, 408, 467, 828, 139, 741]
print(" Selection sort: ", selectionSort(arrayForSelectionSort), "\n")
