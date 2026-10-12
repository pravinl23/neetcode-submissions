class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0 for i in range(n)]
        stack = [] # [tempurature, next warmer]

        i = 0
        for i in range(n):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                prev = stack.pop()
                res[prev] = i - prev
            stack.append(i)

        return res
        
                
