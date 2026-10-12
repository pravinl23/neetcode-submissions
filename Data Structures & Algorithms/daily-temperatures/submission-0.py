class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        stack = []
        res = [0 * 0 for i in range(len(temperatures))]
        for i, t in enumerate(temperatures):
            if not stack:
                stack.append([t, i])
            else:
                while stack and t > stack[-1][0]:
                    prev = stack.pop()
                    res[prev[1]] = i - prev[1]
                stack.append([t, i])

                    
        return res