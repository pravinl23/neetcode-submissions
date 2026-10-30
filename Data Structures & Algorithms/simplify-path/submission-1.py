class Solution:
    def simplifyPath(self, path: str) -> str:
        tokens = path.split("/")
        stack = []
        for t in tokens:
            if not t or t == ".":
                continue

            if t == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(t)

        res = "/" + "/".join(stack)
        return res
