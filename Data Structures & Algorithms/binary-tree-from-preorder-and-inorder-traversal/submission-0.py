# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        in_order_location = {}
        for i,n in enumerate(inorder):
            in_order_location[n] = i
        
        def buildTree(preorder_i, l, r):
            if l > r:
                return None
            m = in_order_location[preorder[preorder_i]]
            node = TreeNode(inorder[m])
            node.left = buildTree(preorder_i + 1, l, m - 1)
            node.right = buildTree(preorder_i + 1 + (m - l), m + 1, r)

            return node

        return buildTree(0, 0, len(preorder) - 1)

