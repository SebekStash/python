#!/usr/bin/python3
def maxHeapify(array, index, heapsize):

    leftChild = 2*index+1
    rightChild = 2*index+2
    largest = index

    if(leftChild < heapsize and array[leftChild] > array[largest]):
        largest = leftChild
   
    if(rightChild < heapsize and array[rightChild] > array[largest]):
        largest = rightChild
    
    if(largest != index):
        array[largest], array[index] = array[index], array[largest]
        maxHeapify(array, largest ,heapsize-1)

# range(start, stop, step)
def heapSort(array, heapsize):
    for i in range(heapsize // 2 - 1, -1, -1):
        maxHeapify(array, i, heapsize)

    for i in range(heapsize-1, 0, -1):
        array[0], array[i] = array[i], array[0]
        maxHeapify(array, 0, i)
    
array = [10,8,6,2,3,5,4,1,7,9]

print(array)
heapSort(array, len(array))
print(array)
