# -*- coding: utf-8 -*-
"""
Created on Mon May 21 11:06:41 2018

@author: Stefan Draghici
"""

"""
The hash table is a data structure that uses a hash function 
to properly store data in specific locations in the table
making inserting, deleteing and searching for items very efficient
"""

class HashTable(object):
    def __init__(self, size):
        # the initial size of the hash table
        self.size=size
        # the hash table will be an initial list of empty slots
        self.slots=[None]*self.size
        # an initial list of data objects equal to the size of the hash table
        self.data=[None]*self.size
        
    """Insert a new data element into the hash table using a specified key"""
    def put(self, key, data):
        # we use the hash function to get the appropiate slot index where we will store the data
        hash_value=self.hash_function(key, len(self.slots))
        # check if the targeted slot is empty, and if it is, 
        # we store ke the key in slots list at the index resulted from the hash funtion call 
        # and the data in the corresponding slot in data list
        if self.slots[hash_value]==None:
            self.slots[hash_value]=key
            self.data[hash_value]=data
        else:
            # if the slot at the hash value index already has the key we want to insert, 
            # we store only the data at the appropiate index
            if self.slots[hash_value]==key:
                self.data[hash_value]=data
            # if the slot is not empty we recalculate the hash value using 
            # the rehash function to obtain a free index
            else:
                new_hash_value=self.rehash(hash_value, len(self.slots))
                # check if the slot at the new hash value index is empty 
                # and doesn't already have the key we want to insert, we get a new index 
                # and store the key and the data at the new index in the hash table,
                # otherwise we replace te old value at that index
                while self.slots[new_hash_value]==None and self.slots[new_hash_value]!=key:
                    next_slot=self.rehash(new_hash_value, len(self.slots))
                if self.slots[next_slot]==None:
                    self.slots[next_slot]=key
                    self.data[next_slot]=data
                else:
                    self.data[next_slot]=data
                    
    """Return the data from the hash table using it's key."""
    def get(self, key):
        # obtain a starting slot by calling the hash function
        start_slot=self.hash_function(key, len(self.slots))
        data=None
        # a marker variable that indicates the searching loop to stop when we found the value
        stop=False
        # a marker variabe that indicates that the searched value has been found
        found=False
        # a marker variabe that indicates the current position
        position=start_slot
        # loop through te entire hash table starting from the slot at the index 
        # indicated by the position variable, and keep going as long as 
        # the slot at the current position is not empty, the value has not been found 
        # and the loop has not been stopped
        while self.slots[position]!=None and not found and not stop:
            # check if the slot at the current position contains the searched key
            if self.slots[position]==key:
                # if we found it, set the found variable to True, 
                # store the data at that index into local data variable
                found=True
                data=self.data[position]
            else:
                # else, rehash the current position to obtain a new index
                position=self.rehash(position, len(self.slots))
                # also check if the current position index is the starting position,
                # and if it is the case, stop the loop
                if position==start_slot:
                    stop=True
        # return the data we wew looking for
        return data
        
    """Return the index of the appropiate slot for inserting a key and the corresponding data. 
       The function takes the key of the data and the size of hash table, and returns 
       the index for insertion as the remainder of the key divided by the size of the hash table."""
    def hash_function(self, key, size):
        return key%size
    
    """If the hash function returns the same index for two or mode entries, there will be a collision.
       If that is the case the rehash function will recalculate the old hash value 
       and return a different free index for the new entry."""
    def rehash(self, old_hash_value, size):
        return (old_hash_value+1)%size
    
    def __getitem__(self, key):
        return self.get(key)
    
    def __setitem__(self, key, data):
        self.put(key, data)
        
# test
h=HashTable(5)
h[0]={'zero':0}
h[1]=8
h[2]='doi'
h[3]=True
h[4]=[3, 2, 1]

print(h.get(0))
print(h.get(1))
print(h.get(2))
print(h.get(3))
print(h.get(4))












