class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0 for i in range(n)]
        stack = [] # [tempurature, next warmer]

        i = 0
        while i < n - 1:
            if not stack:
                stack.append(i)
                continue
            j = i + 1
            while stack and j < n and temperatures[stack[-1]] < temperatures[j]:
                prev = stack.pop()
                res[prev] = j - prev
            stack.append(j)
            i = j

        return res
        
                
