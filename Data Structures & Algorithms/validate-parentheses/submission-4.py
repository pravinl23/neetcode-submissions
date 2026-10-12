class Solution:
    def isValid(self, s: str) -> bool:
        
        mapping = { 
            ']' : '[',
            '}' : '{',
            ')' : '('
        }

        stack = []
        for char in s:
            print(stack)
            if not stack:
                stack.append(char)
            elif char not in mapping:
                stack.append(char)
            elif char in mapping and mapping[char] != stack[-1]:
                return False
            else:
                stack.pop()
        
        return True if not stack else False
