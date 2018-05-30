#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 18 16:11:43 2018

@author: user
"""

"""
The Queue is a data structure that adds new elements a the front 
and deletes old elements from the rear (FIFO)
"""

class Queue(object):
    def __init__(self):
        # we will use the python list as a basic structure for our stack
        self.items=[]
        
    """check if the stack is empty or not"""
    def is_empty(self):
        return self.items==[]
    
    """insert an element at the start of the queue and push the rest of the elements"""
    def enqueue(self, item):
        self.items.insert(0, item)
      
    """remove the first inserted element and return it"""
    def dequeue(self):
        return self.items.pop()
    
    """return the size of the stack"""
    def size(self):
        return len(self.items)
    
# test the queue
queue=Queue()
print(queue.is_empty())
print(queue.size())
queue.enqueue(8)
queue.enqueue(18)
print(queue.size())
queue.enqueue(29)
queue.dequeue()