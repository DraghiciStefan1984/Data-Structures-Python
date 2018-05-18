#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 18 16:11:43 2018

@author: user
"""

"""
The Deque is a data structure similar to a queue, but with no restrictions 
regarding adding or deleting items.
"""

class Deque(object):
    def __init__(self):
        # we will use the python list as a basic structure for our dequeue
        self.items=[]
        
    """check if the dequeue is empty or not"""
    def is_empty(self):
        return self.items==[]
    
    """add an item to the front of de the deque"""
    def add_front(self, item):
        self.items.append(item)
        
    """add an item to the rear of de the deque"""
    def add_rear(self, item):
        self.items.insert(0, item)
        
    """remove an item from the front and return it"""
    def remove_front(self):
        return self.items.pop()
    
    """remove an item from the rear and return it"""
    def remove_rear(self):
        return self.items.pop(0)
    
    """return the size of the deque"""
    def size(self):
        return len(self.items)
    
# test the deque
d=Deque()
d.add_front("hello")
d.add_rear("x")
d.add_front("w")
print(d.size())
print(d.remove_front()+" "+d.remove_rear())



