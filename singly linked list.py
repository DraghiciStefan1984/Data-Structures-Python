# -*- coding: utf-8 -*-
"""
Created on Sat May 19 23:46:46 2018

@author: Stefan Draghici
"""

"""The singly linked list represeznt a list of elements that store a value and a reference to the next element"""

"""The linked list can be represented by a series of nodes"""
class Node(object):
    def __init__(self, value):
        # the value to be stoerd in the node
        self.value=value
        # the reference to the next node, for the moment is None
        self.nextnode=None
        
# test the singly linked list
a=Node(1)
b=Node(2)
c=Node(3)
d=Node(4)
e=Node(5)

a.nextnode=b
b.nextnode=c
c.nextnode=d
d.nextnode=e
e.nextnode=a

print(a.value)
print(a.nextnode.value)

print(b.value)
print(b.nextnode.value)

print(c.value)
print(c.nextnode.value)