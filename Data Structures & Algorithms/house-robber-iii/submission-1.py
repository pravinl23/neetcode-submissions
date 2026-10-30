# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node):
            if not node:
                return 0, 0
            firstleft, secondleft = dfs(node.left)
            firstright, secondright = dfs(node.right)
            f = max(node.val + secondright +secondleft, firstleft + firstright)
            s = firstleft + firstright

            return f, s


        first, second = dfs(root)
        return max(first, second)