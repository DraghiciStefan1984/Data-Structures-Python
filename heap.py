# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 09:47:07 2018

@author: Stefan Draghici
"""

"""A data structure that allows a limited number of items stored in order of priority."""
class Heap(object):
    # the maximum number of items we store in the heap
    HEAP_SIZE=10
    
    def __init__(self):
        # initialize the heap as a list of slots with 0 as initial value
        self.heap=[0]*Heap.HEAP_SIZE
        # the index of the first position
        self.current_position=-1
        
    """Insert a new item into the heap."""
    def insert(self, item):
        # if the heap is full we cannot insert a new item
        if self.is_full():
            print("heap is full, cannot insert a new item.")
            return
        # if it isn't, jump to the next position and assign the item into the slot
        self.current_position+=1
        self.heap[self.current_position]=item
        # check if the insetion violates the heap contitions
        self.fix_up(self.current_position)
    
    """Check if the heap is full."""
    def is_full(self):
        # if the current position is equal to the heap size, return true
        if self.current_position==Heap.HEAP_SIZE:
            return True
        else:
            return False
    
    """Verify if the index violates the heap properties."""
    def fix_up(self, index):
        # calculate the appropiate index for each element
        parent_index=(index-1)//2
        while parent_index>=0 and self.heap[parent_index]<self.heap[index]:
            temp=self.heap[index]
            self.heap[index]=self.heap[parent_index]
            self.heap[parent_index]=temp
            parent_index=(index-1)//2
            
    """Verify if the index violates the heap properties."""
    def fix_down(self, index, up_to_index):
        while index<=up_to_index:
            left_child=2*index+1
            right_child=2*index+2
            if left_child<up_to_index:
                child_to_swap=None
                if right_child>up_to_index:
                    child_to_swap=left_child
                else:
                    if self.heap[left_child]>self.heap[right_child]:
                        child_to_swap=left_child 
                    else:
                        child_to_swap=right_child
                if self.heap[index]<self.heap[child_to_swap]:
                    temp=self.heap[index]
                    self.heap[index]=self.heap[child_to_swap]
                    self.heap[child_to_swap]=temp
                else:
                    break
                index=child_to_swap
            else:
                break
            
    """Sort the items in order."""
    def heapsort(self):
        for i in range(0, self.current_position+1):
            # at the begining, the root node will have the maximum value
            temp=self.heap[0]
            print(temp)
            # update the maximum heap value
            self.heap[0]=self.heap[self.current_position-i]
            self.heap[self.current_position-i]=temp
            self.fix_down(0, self.current_position-i-1)

# test
heap=Heap()
heap.insert(8)
heap.insert(9)
heap.insert(10)
heap.insert(4)
heap.insert(3)
print(heap)



