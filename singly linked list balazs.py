#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 29 16:43:00 2018

@author: user
"""

class Node(object):
    def __init__(self, data):
        # the data we want to insert
        self.data=data
        # reference to the next node in the list
        self.next_node=None
        
class LinkedList(object):
    def __init__(self):
        # the first node in the list
        self.head=None
        # the size of the list
        self.size=0
        
    """Insert an element at the beginig of the list."""
    def insert_start(self, data):
        # first, increment the size of the list
        self.size+=1
        # instantiate a new node with the data we want to insert
        new_node=Node(data)
        # if there is no head node in the list, we set the new node to be the head of the list,
        # if not, we the set a reference from the new node to the old head node 
        # and set the new node to be head
        if not self.head:
            self.head=new_node
        else:
            new_node.next_node=self.head
            self.head=new_node
            
    """Return the size of the list. O(1)"""
    def size(self):
        return self.size
    
    """Returns the size of the list after iterating. O(N)"""
    def size_iter(self):
        # starting from the head node and the initial size counter of 0
        # go through the whole list and increment the size counter
        actual_node=self.head
        size=0
        while actual_node is not None:
            size+=1
            actual_node=actual_node.next_node
        return size
    
    """Insert an element at the end of the list."""
    def insert_end(self, data):
        # first, increment the size of the list
        self.size+=1
        # instantiate a new node with the data we want to insert
        new_node=Node(data)
        # the current node will be the head
        actual_node=self.head
        # traverse the list to see if the next node exists, update the reference to the current node
        # we want to find the end of the list
        while actual_node.next_node is not None:
            actual_node=actual_node.next_node
        # when we find the last node, we store the reference 
        # to the node we want to insert at the end of the list
        actual_node.next_node=new_node
        
    """Traverse through the whole list."""
    def traverse(self):
        # start from the beginning of the list
        actual_node=self.head
        while actual_node is not None:
            # print the data stored at the current node, and jump to the next node
            print("%d"%actual_node.data)
            actual_node=actual_node.next_node
            
    """Remove a ode from the list."""
    def remove(self, data):
        # if we have an empty list, we exit
        if self.head is None:
            return
        # else, we decrement the size of the list
        self.size-=1
        # store a reference to the head node and set the previous node to be None for the begining
        current_node=self.head
        previous_node=None
        # keep iterating the list if we haven't found the node that contains the data we want to delete
        # adn update the current node to be the previous node
        while current_node.data != data:
            previous_node=current_node
            current_node=current_node.next_node
        if previous_node is None:
            self.head=current_node.next_node
        else:
            previous_node.next_node=current_node.next_node
            
# test
linked_list=LinkedList()
linked_list.insert_start(8)
linked_list.insert_start(9)
linked_list.insert_end(18)
print(linked_list.size_iter())
linked_list.traverse()
print("==========")
linked_list.remove(9)
linked_list.traverse()