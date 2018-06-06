#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  4 13:15:29 2018

@author: user
"""

"""The Node class will store the data and will be the building block of AVL tree."""
class Node(object):
    def __init__(self, data):
        # the data 
        self.data=data
        # the height of the tree (number of layers of nodes)
        self.height=0
        self.left_child=None
        self.right_child=None
        
"""The AVL tree class will represent a balanced tree."""
class AVL(object):
    def __init__(self):
        # init the root node
        self.root=None
        
    """Calculate the height of a node."""
    def calculate_height(self, node):
        # if the node doesn't exist the height will be -1
        if not node:
            return -1
        return node.height
    
    """
        Check if the tree is balanced at given the node. 
        If the result > 1 => left heavy tree => right rotation.
        If the result < -1 => right heavy tree => left rotation.
    """
    def calculate_balance(self, node):
        if not node:
            return 0
        return self.calculate_height(node.left_child)-self.calculate_height(node.right_child)
    
    """Make a rotation to the right."""
    def rotate_right(self, node):
        print("Rotating to the right at node: ", node.data)
        # make the right rotation
        temp_left_child=node.left_child
        t=temp_left_child.right_child
        temp_left_child.right_child=node
        node.left_child=t
        # calculate the new height of the node
        node.height=max(self.calculate_height(node.left_child), self.calculate_height(node.right_child))+1
        temp_left_child.height=max(self.calculate_height(temp_left_child.left_child), self.calculate_height(temp_left_child.right_child))+1
        # after the rotation, the temporary node will be the root node
        return temp_left_child
    
    """Make a rotation to the left."""
    def rotate_left(self, node):
        print("Rotating to the left at node: ", node.data)
        # make the right rotation
        temp_right_child=node.right_child
        t=temp_right_child.left_child
        temp_right_child.left_child=node
        node.right_child=t
        # calculate the new height of the node
        node.height=max(self.calculate_height(node.left_child), self.calculate_height(node.right_child))+1
        temp_right_child.height=max(self.calculate_height(temp_right_child.left_child), self.calculate_height(temp_right_child.right_child))+1
        # after the rotation, the temporary node will be the root node
        return temp_right_child
    
    """Insert a new element into the tree."""
    def insert(self, data):
        self.root=self.insert_node(data, self.root)
       
    """Insert a new node into the tree."""
    def insert_node(self, data, node):
        # check if the node we want to insert is already in the tree,
        # if not, create and return it
        if not node:
            return Node(data)
        # insert the data into the appropiate slot in the tree
        if data<node.data:
            node.left_child=self.insert_node(data, node.left_child)
        else:
            node.right_child=self.insert_node(data, node.right_child)
        node.height=max(self.calculate_height(node.left_child), self.calculate_height(node.right_child))+1
        return self.settle_violations(data, node)
    
    """Settle the violations of the AVL tree rules."""
    def settle_violations(self, data, node):
        # check if the tree is balanced at the given node
        balance=self.calculate_balance(node)
        # case 1: left left heavy 
        if balance>1 and data<node.left_child.data:
            print("left left heavy")
            return self.rotate_right(node)
        # case 2: right right heavy 
        if balance<-1 and data>node.right_child.data:
            print("right righr heavy")
            return self.rotate_left(node)
        # case 3: left heavy 
        if balance>1 and data>node.left_child.data:
            print("left right heavy")
            node.left_child=self.rotate_left(node.left_child)
            return self.right_child(node)
        # case 4: right left heavy 
        if balance<-1 and data>node.right_child.data:
            print("right left heavy")
            node.right_child=self.rotate_right(node.right_child)
            return self.rotate_left(node)
        return node
        
    """Traverse the entire AVL tree starting at a given node."""
    def traverse(self):
        if self.root:
            self.traverse_in_order(self.root)
    
    def traverse_in_order(self, node):
        if node.left_child:
            self.traverse_in_order(node.left_child)
        print(node.data)
        if node.right_child:
            self.traverse_in_order(node.right_child)
            
    
        
# test
avl=AVL()
avl.insert(8)
avl.insert(9)
avl.insert(7)
avl.insert(10)
avl.insert(18)
avl.insert(19)
print(avl.traverse())



