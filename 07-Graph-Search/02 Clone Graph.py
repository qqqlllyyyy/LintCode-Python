# Clone Graph
# Clone an undirected graph. Each node in the graph contains 
# a label and a list of its neighbors.
#
# OJ's undirected graph serialization:
# Nodes are labeled uniquely.
# We use # as a separator for each node, and , as a separator for node
# label and each neighbor of the node.
# As an example, consider the serialized graph {0,1,2#1,2#2,2}.
# The graph has a total of three nodes, and therefore contains three parts
# as separated by #.
# 1. First node is labeled as 0. Connect node 0 to both nodes 1 and 2.
# 2. Second node is labeled as 1. Connect node 1 to node 2.
# 3. Third node is labeled as 2. Connect node 2 to node 2 (itself), thus forming a self-cycle.
#
"""
  Definition for a undirected graph node
  class UndirectedGraphNode:
      def __init__(self, x):
          self.label = x
          self.neighbors = []
"""
class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def __init__(self):
        self.dict = {}
        
    def cloneGraph(self, node):
        if node == None: return None
        nodes = []
        map = {}
        nodes.append(node)
        
        # Traverse all nodes and clone nodes.
        map[node] = UndirectedGraphNode(node.label)
        start = 0
        while start < len(nodes):
            head = nodes[start]
            for i in range(len(head.neighbors)):
                neighbor = head.neighbors[i]
                if neighbor not in map:
                    map[neighbor] = UndirectedGraphNode(neighbor.label)
                    nodes.append(neighbor)
            start += 1
        
        # Then clone all the neighbors.
        for i in range(len(nodes)):
            newNode = map[nodes[i]]
            for j in range(len(nodes[i].neighbors)):
                newNode.neighbors.append(map[nodes[i].neighbors[j]])
        
        return map[node]
    
    
        
