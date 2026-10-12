# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:


        # make p > q
        if p.val < q.val:
            temp = p
            p = q
            q = temp
        

        while root:
            if p.val >= root.val and q.val <= root.val:
                return root
            elif p.val > root.val and q.val > root.val:
                root = root.right
            else:
                root = root.left
        

        