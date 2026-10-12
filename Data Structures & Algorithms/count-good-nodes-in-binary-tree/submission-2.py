# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0
        def dfs(node, m):
            nonlocal res
            if not node:
                return
            if node.val >= m:
                res += 1
            dfs(node.right, max(m, node.val))
            dfs(node.left, max(m, node.val))

        dfs(root, root.val)
        return res