# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def recurse(r, l, h):
            if not r:
                return True
            if not l < r.val < h:
                return False
            return recurse(r.left, l, r.val) and recurse(r.right, r.val, h)


        return recurse(root, -1000000001, 1000000001)