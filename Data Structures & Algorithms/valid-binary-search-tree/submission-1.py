# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        def traverse(root, low, high):
            if not root:
                return True
            
            if root.val >= high or root.val <= low:
                return False

            
            return traverse(root.left, low, root.val) and traverse(root.right, root.val, high)

        return traverse(root, float('-inf'), float('inf'))
