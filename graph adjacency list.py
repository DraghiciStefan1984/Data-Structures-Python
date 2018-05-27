# -*- coding: utf-8 -*-
"""
Created on Sun May 27 10:33:05 2018

@author: Stefan Draghici
"""

"""
The graph is a data structure similar to a tree, except that paths 
can exists between an unrestricted number of nodes.
It can be implemented as an adjacencny list of condected nodes.
"""

# The Vertex class represent the structure that stores the connected nodes,
# that will be the building block of the Graph 
class Vertex(object):
    def __init__(self, key):
        self.id=key
        self.connected_to={}
       
    """Add neighbors to the current node with a certain weight"""
    def add_neighbor(self, neighbor, weight=0):
        # append the weight to the connected_to dictionary at the index indicated by the neighbor
        self.connected_to[neighbor]=weight
        
    """Return all the connections from the connected_to dictionary."""
    def get_connections(self):
        return self.connected_to.keys()
    
    """Return the id of the current connection"""
    def get_id(self):
        return self.id
    
    """Return the weight of the current connection's neighbor"""
    def get_weight(self,neighbor):
        return self.connected_to[neighbor]
    
    """Return the string representation of the connection"""
    def __str__(self):
        return str(self.id)+" connected to "+str([x.id for x in self.connected_to])
    
"""The Graph class will build the actual graph from Vertices"""
class Graph(object):
    def __init__(self):
        # we will need a dictionary of vertices
        self.vertex_list={}
        # the number of vertices in the graph
        self.num_vertices=0
        
    """Add a Vertex to the graph and return it."""
    def add_vertex(self, key):
        # increment the number of vertices
        self.num_vertices+=1
        # add the new vertex to the dictionary at the specified key
        new_vertex=Vertex(key)
        self.vertex_list[key]=new_vertex
        return new_vertex
    
    """Return a vertex from the list."""
    def get_vertex(self, vertex):
        # check of the vertex exists in the dictionary
        if vertex in self.vertex_list:
            return self.vertex_list[vertex]
        else:
            return None
        
    """Add an edge that connects two vertices, with a certain cost."""
    def add_edge(self, from_vertex, to_vertex, cost=0):
        # if the starting and ending vertices are not in the dictionary, 
        # we add them by calling the add method
        if from_vertex not in self.vertex_list:
            new_vertex=self.add_vertex(from_vertex)
        if to_vertex not in self.vertex_list:
            new_vertex=self.add_vertex(to_vertex)
        # after we have the starting and ending vertoces we add the edge between them
        self.vertex_list[from_vertex].add_neighbor(self.vertex_list[to_vertex], cost)
    
    """Return the vertices from the graph."""
    def get_vertices(self):
        return self.vertex_list.keys()
    
    """Return the values from the dictionary. """
    def __iter__(self):
        return iter(self.vertex_list.values())
    
    """Check if a vertex is in the dictionary."""
    def __contains__(self, vertex):
        return vertex in self.vertex_list
    
# test
g=Graph()

for i in range(8):
    g.add_vertex(i)
    
print(g.vertex_list.keys())

g.add_edge(0, 3, 88)
g.add_edge(1, 6, 18)  

for vertex in g:
    print(vertex)
    print(vertex.get_connections())
    