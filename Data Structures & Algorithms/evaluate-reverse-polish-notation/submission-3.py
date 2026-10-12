class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        symbol = ["+","-","*","/"]
        for t in tokens:
            if t in symbol:
                a = int(stack.pop())
                b = int(stack.pop())
                if t == "+":
                    stack.append(a + b)
                elif t == "-":
                    stack.append(b - a)
                elif t == "*":
                    stack.append(a * b)
                elif t == "/":
                    stack.append(b / a)
            else:
                stack.append(t)

        print(stack)
        return int(stack[0])

            