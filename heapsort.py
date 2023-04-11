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
