# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        def traverse(node, maxsofar):
            if not node:
                return 0
            if node.val >= maxsofar:
                return 1 + traverse(node.left, node.val) + traverse(node.right, node.val)
            else:
                return traverse(node.left, maxsofar) + traverse(node.right, maxsofar)

        return traverse(root, root.val)