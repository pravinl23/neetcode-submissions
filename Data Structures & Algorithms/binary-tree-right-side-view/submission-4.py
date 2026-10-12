# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        buckets = [[]]

        def recurse(node, height):
            if not node:
                return
            if height > (len(buckets) - 1):
                buckets.append([])

            buckets[height].append(node.val)
            recurse(node.left, height + 1)
            recurse(node.right, height + 1)

        recurse(root, 0)

        res = []
        for b in buckets:
            last = b.pop()
            res.append(last)

        return res
        
