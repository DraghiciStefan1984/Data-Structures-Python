# -*- coding: utf-8 -*-
"""
Created on Fri May 18 12:38:14 2018

@author: Stefan Draghici
"""

# the Stack is a data structure that stores the elemnts using FIFO (first in first out)
class Stack(object):
    def __init__(self):
        # we will use the python list as a basic structure for our stack
        self.items=[]
        
    """check if the stack is empty or not"""
    def is_empty(self):
        return self.items==[]
    
    """append items at the top of the stack"""
    def push(self, item):
        self.items.append(item)
        
    """remove the item at the top of the stack and returns it"""
    def pop(self):
        self.items.pop()
        
    """return = the item at the top of the stack"""
    def peek(self):
        return self.items[len(self.items)-1]
    
    """return the size of the stack"""
    def size(self):
        return len(self.items)
    
# test the stack
stack=Stack()
print(stack.is_empty())
stack.push(5)
stack.push(8)
stack.push(9)
print(stack.size())
print(stack.is_empty())
print(stack.peek())
print(stack.pop())
print(stack.peek())
print(stack.size())