"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        clone_map = {}
        clone_map[None] = None

        def dfs(cur_node):
            if not cur_node:
                return None
            if cur_node not in clone_map:
                new_node = Node(cur_node.val)
                clone_map[cur_node] = new_node
            else:
                new_node = clone_map[cur_node]

            for neigh in cur_node.neighbors:
                if neigh in clone_map:
                    new_node.neighbors.append(clone_map[neigh])
                else:
                    new_node.neighbors.append(dfs(neigh))
            
            return new_node

        cloned_node = dfs(node)
        return cloned_node






        