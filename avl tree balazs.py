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
        Check if the tree is balanced. 
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













