# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        res = True
        def dfs(node):
            nonlocal res
            if not node:
                return -1
            l = 1 + dfs(node.left)
            r = 1 + dfs(node.right)
            res = (abs(l - r) < 2) and res
            return max(l, r)
        dfs(root)
        return res