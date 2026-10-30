class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        stack = [(root, False)]

        while stack:
            node, seen = stack.pop()
            if not node:
                continue
            if seen:
                res.append(node.val)
            else:
                stack.append([node, True])
                stack.append([node.right, False])
                stack.append([node.left, False])
                
        return res