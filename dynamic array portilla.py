# -*- coding: utf-8 -*-
"""
Created on Fri May 18 11:58:36 2018

@author: Stefan Draghici
"""

# import the ctypes library
import ctypes

"""
A dynamic array is and array that can change it's size dynamically to store
an increasing number of elements
"""
class DynamicArray(object):
    def __init__(self):
        # the count of the elements
        self.n=0
        # the number of elements it can accept (1 by default)
        self.capacity=1
        # the actual array of element build with the specified capacity
        self.A=self.make_array(self.capacity)
        
    """the special method that returns the length of the array"""
    def __len__(self):
        return self.n
    
    """the special method that returns the element at a certain index"""
    def __getitem__(self, k):
        # first, chek if the index k is within the array's bounds
        if not 0<=k<self.n:
            # if the k index is outside the array's bounds we return an IndexError 
            return IndexError('K is out of bounds!')
        else:
            # if the k index is within the array's bounds we return the value/object stored in the array at index k
            return self.A[k]
        
    """the method that adds elements at the end of the array"""
    def append(self, element):
        # firts we check to see if the number of elements has reached the maximum capacity of the array
        # and if it has, we double the capacity using the private method _resize
        if self.n==self.capacity:
            self._resize(2*self.capacity)
        # after resize, we store the element at the last index of the array and increment the counter variable n
        self.A[self.n]=element
        self.n+=1
        
    """the method that removes the last element of the array and decrements the count"""
    def remove(self):
        self.A[self.n-1]=None
        self.n-=1
        
    """the method that resizes the capacity of ot has been reached"""
    def _resize(self, new_capacity):
        # first we build a new array with the new capacity
        B=self.make_array(new_capacity)
        
        # we copy all the elemnts from the original array into the new array of increased size
        for k in range(self.n):
            B[k]=self.A[k]
        # we overwrite the original array with the new array B of increased size
        self.A=B
        # the original capacity will be updated
        self.capacity=new_capacity
        
    """the method that builds an array pf a specified capacity"""
    def make_array(self, new_capacity):
        return (new_capacity*ctypes.py_object)()
        
# test the array
arr=DynamicArray()

arr.append(1)
print(len(arr))        
arr.append(2)
arr.append(3)
arr.append(4)       
print(len(arr))     
arr.remove()   
print(len(arr))         
        
        
        
        
        
        
        
        
        