# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        path = []
        def dfs(root, h):
            if not root:
                return
            if len(path) - 1 < h:
                path.append([])
            if not path[h]:
                path[h].append(root.val)

            dfs(root.right, h + 1)
            dfs(root.left, h + 1)


        dfs(root, 0)
        return [x[0] for x in path]