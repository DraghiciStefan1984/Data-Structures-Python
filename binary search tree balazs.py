#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 31 18:14:06 2018

@author: user
"""

class Node(object):
    def __init__(self, data):
        # the data we want to store
        self.data=data
        # the reference to the left child
        self.left_child=None
        # the reference to the right child
        self.right_child=None
        
class BinarySearchTree(object):
    def __init__(self):
        # the root node
        self.root=None
        
    """Insert a new element into the tree."""
    def insert(self, data):
        # first, check if the root node exists, and if it does not exist, 
        # we create it and store de value
        if not self.root:
            self.root=Node(data)
        else:
        # if there is a root node, we insert the new node accordingly
            self.insert_node(data, self.root)
            
    """Insert a new node into the tree."""
    def insert_node(self, data, node):
        # chek if the data we want to insert is smaller or greater 
        # than the data stored in the current node, and store it in the right place
        if data<node.data:
            if node.left_child:
                self.insert_node(data, node.left_child)
            else:
                node.left_child=Node(data)
        if data>node.data:
            if node.right_child:
                self.insert_node(data, node.right_child)
            else:
                node.right_child=Node(data)
                
    """Return the minimum value from the tree."""
    def get_min_value(self):
        # check if the tree has nodes
        if self.root:
            return self.get_min(self.root)
        
    """Return the minimum value from a node."""
    def get_min(self, node):
        # chek if there is a left child that contains the lesser values, 
        # and the return the minimum, else return the data.
        if node.left_child:
            return self.get_min(node.left_child)
        return node.data
    
    """Return the maximum value from the tree."""
    def get_max_value(self):
        # check if the tree has nodes
        if self.root:
            return self.get_max(self.root)
        
    """Return the maximum value from a node."""
    def get_max(self, node):
        # chek if there is a right child that contains the greater values, 
        # and the return the maximum, else return the data.
        if node.right_child:
            return self.get_max(node.right_child)
        return node.data
        
    """Traverse the tree."""
    def traverse(self):
        if self.root:
            self.traverse_in_order(self.root)
            
    """Traverse the tree starting from the root node."""
    def traverse_in_order(self, node):
        if node.left_child:
            self.traverse_in_order(node.left_child)
        print("%s"%node.data)
        if node.right_child:
            self.traverse_in_order(node.right_child)
            
    """Remove a node from the tree."""
    def remove(self, data):
        if self.root:
            self.root=self.remove_node(data, self.root)
            
    def remove_node(self, data, node):
        if not node:
            return node
        if data<node.data:
            node.left_child=self.remove_node(data, node.left_child)
        elif data>node.data:
            node.right_child=self.remove_node(data, node.right_child)
        else:
            if not node.left_child and not node.right_child:
                print("removing leaf node...")
                del node
                return None
            if not self.left_child:
                print("removing node with single right child...")
                temp_node=node.right_child
                del node
                return temp_node
            if not self.left_child:
                print("removing node with single left child...")
                temp_node=node.left_child
                del node
                return temp_node
        print("removing node with two childern...")
        temp_node=self.get_predecesor(node.left_child)
        node.data=temp_node.data
        node.left_child=self.remove_node(temp_node.data, node.left_child)
        
    def get_predecesor(self, node):
        if node.right_child:
            return self.get_predecesor(node.right_child)
        return node
                
        
# test
tree=BinarySearchTree()  
tree.insert(8)
tree.insert(18)
tree.insert(9)
tree.insert(19)
tree.insert(3)
tree.insert(33)
print(tree.get_max_value())
print(tree.get_min_value())
tree.traverse()