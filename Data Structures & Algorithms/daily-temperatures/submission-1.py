class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        stack = [] # [tempurature, next warmer]
        for i in range(len(temperatures) - 1, -1, -1):
            if not stack:
                stack.append([temperatures[i], 0])
                continue
            prev = 1
            n = len(stack)
            while stack[-prev][0] > temperatures[i] or stack[-prev][1] != 0:
                if stack[-prev][0] > temperatures[i]:
                    stack.append([temperatures[i], prev])
                    break
                else:
                    prev += stack[-prev][1]
            
            if stack[-prev][1] == 0:
                stack.append([temperatures[i], 0])

        res = []
        for i in range(len(stack) - 1, -1, -1):
            res.append(stack[i][1])
        return res
                
