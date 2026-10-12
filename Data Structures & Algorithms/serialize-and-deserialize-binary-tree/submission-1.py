# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []
        def dfs(node):
            if not node:
                res.append("None")
                return
            res.append(node.val)
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        s = ""
        for r in res:
            s += str(r) + "#"
        return s
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        data = data.split("#")
        n = len(data)
        data = deque(data)
        def dfs():
            if not data:
                return None
            n = data.popleft()
            if n == "None":
                return None
            
            node = TreeNode(n)
            node.left = dfs()
            node.right = dfs()

            return node
        return dfs()
