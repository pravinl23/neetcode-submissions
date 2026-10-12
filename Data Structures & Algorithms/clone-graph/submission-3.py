"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        nodeMapping = {None : None}
        def dfs(root):
            if not root:
                return None
            if root.val in nodeMapping:
                return nodeMapping[root.val]
            
            newNode = Node(root.val)
            nodeMapping[root.val] = newNode
            for n in root.neighbors:
                newNode.neighbors.append(dfs(n))

            return newNode

        return dfs(node)