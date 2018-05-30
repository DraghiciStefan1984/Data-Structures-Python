#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 30 17:44:00 2018

@author: user
"""
"""A data structure that functions according to the LIFO principle."""
class Stack(object):
    def __init__(self):
        # initialize the stack as an one dimention empty array
        self.stack=[]
        
    """Check if the stack is empty or not."""
    def is_empty(self):
        return self.stack==[]
    
    """Insert a new element on top of the stack."""
    def push(self, data):
        self.stack.append(data)
        
    """Remove the element on top of the stack and return it."""
    def pop(self):
        data=self.stack[-1]
        del self.stack[-1]
        return data
    
    """Return the element on top of the stack."""
    def peek(self):
        return self.stack[-1]
    
    """Return the size of the stack."""
    def size(self):
        return len(self.stack)
    
# test
s=Stack()
print(s.is_empty())
s.push(8)
s.push(18)
s.push(19)
print(s.is_empty())
print(s.peek())
print(s.pop())
print(s.peek())