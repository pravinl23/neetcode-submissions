class Solution:
    def decodeString(self, s: str) -> str:
        num = set(str(x) for x in range(10))
        charstack = []
        numstack = []
        n = ""
        for ch in s:
            if ch in num:
                n += ch
            elif ch == "]":
                token = deque()
                while charstack[-1] != "[":
                    token.appendleft(charstack.pop())
                charstack.pop()
                charstack.append(int(numstack.pop()) * "".join(token))
            else:
                if n:
                    numstack.append(n)
                n = ""
                charstack.append(ch)
        return "".join(charstack)
            