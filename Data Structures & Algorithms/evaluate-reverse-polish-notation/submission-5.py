class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = ["+", "-", "*", "/"]
        stack = []
        for t in tokens:
            if t in operators:
                n2, n1 = int(stack.pop()), int(stack.pop())
                if t == "+":
                    stack.append(n2 + n1)
                elif t == "-":
                    stack.append(n1 - n2)
                elif t == "*":
                    stack.append(n1 * n2)
                elif t == "/":
                    stack.append(n1 / n2)
            else:
                stack.append(t)

        return int(stack[0])