# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = 0
        answer = None

        def recurse(r):
            nonlocal count, answer

            if not r:
                return 
            if answer is not None:
                return
            
            recurse(r.left)

            count += 1
            if count == k:
                answer = r.val
                return
            
            recurse(r.right)

        recurse(root)
        return answer
        