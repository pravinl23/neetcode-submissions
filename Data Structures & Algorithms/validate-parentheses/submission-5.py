class Solution:
    def isValid(self, s: str) -> bool:
        closeToOpen = { '}' : '{', ")": "(", "]" : "["}
        stack = []

        for p in s:
            # its an opening brace so add it
            if p not in closeToOpen:
                stack.append(p)
            # its a closing brace so check if its valid
            else:
                if not stack or closeToOpen[p] != stack.pop():
                    return False

        return True if not stack else False