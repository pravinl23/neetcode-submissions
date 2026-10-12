# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        a = []
        def dfs(node):
            if not node:
                return None
            
            s1 = dfs(node.left)
            s2 = dfs(node.right)
            if s1 is not None and s2 is not None:
                potential = [s1 + s2 + node.val, node.val + s1, node.val + s2, node.val]
            elif s1 is not None:
                potential = [node.val + s1, node.val]
            elif s2 is not None:
                potential = [node.val + s2, node.val]
            else:
                potential = [node.val]
            a.append(max(potential))

            straight = node.val
            if s1 is not None:
                straight = max(straight, node.val + s1)
            if s2 is not None:
                straight = max(straight, node.val + s2)
            return straight

    
        dfs(root)
        return max(a)