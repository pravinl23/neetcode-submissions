# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        
        def dfs(node):
            if not node:
                return 0
            
            l, r = dfs(node.left), dfs(node.right)
            if l == -target:
                node.left = None
                l = 0
            if r == -target:
                node.right = None
                r = 0       
            
            if l == r == 0:
                return -node.val
            
            return node.val

        k = TreeNode(0, root)
        dfs(k)


        return k.left
                