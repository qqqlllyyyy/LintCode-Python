# Topological Sorting
# Given an directed graph, a topological order of the graph nodes 
# is defined as follow:
# 1. For each directed edge A -> B in graph, A must before B in the
#    order list.
# 2. The first node in the order can be any node in the graph with
#    no nodes direct to it.
# Find any topological order for the given graph.
#
# Note
# You can assume that there is at least one topological order in the graph.
#
"""
    Definition for a Directed graph node
    class DirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
"""
class Solution:
    """
    @param graph: A list of Directed graph node
    @return: A list of integer
    """
    def topSort(self, graph):
        # write your code here
        result = []
        map = {}
        # Count in-degree for all nodes in the graph
        for node in graph:
            for neighbor in node.neighbors:
                if neighbor in map:
                    map[neighbor] += 1
                else:
                    map[neighbor] = 1
        
        q = []
        for node in graph:
            if node not in map:
                q.append(node)
                result.append(node)
        
        while len(q) > 0:
            node = q.pop(0)
            for neighbor in node.neighbors:
                map[neighbor] -= 1
                # A node can be appended in the result only if all nodes 
                # pointing to it has been selected before!
                if map[neighbor] == 0: 
                    q.append(neighbor)
                    result.append(neighbor)
        
        return result
