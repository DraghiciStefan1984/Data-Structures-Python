#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 30 17:44:00 2018

@author: user
"""
"""A data structure that functions according to the FIFO principle."""
class Queue(object):
    def __init__(self):
        # initialize the queue as an one dimention empty array
        self.queue=[]
        
    """Check if the queue is empty or not."""
    def is_empty(self):
        return self.queue==[]
    
    """Insert a new element into the queue."""
    def enqueue(self, data):
        self.queue.append(data)
        
    """Remove the first element from the queue and return it."""
    def deque(self):
        data=self.queue[0]
        del self.queue[0]
        return data
    
    """Return tthe first element from the queue."""
    def peek(self):
        return self.queue[0]
    
    """Return the size of the stack."""
    def size(self):
        return len(self.queue)
    
# test
q=Queue()
print(q.is_empty())
q.enqueue(8)
q.enqueue(18)
q.enqueue(19)
print(q.is_empty())
print(q.deque())
print(q.peek())