class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        m = max(heights)
        for i, h in enumerate(heights):
            if not stack:
                stack.append([i, h])
                continue
            start = i
            while stack and stack[-1][1] >= h:
                popped = stack.pop()
                m = max(popped[1] * (i - popped[0]), m)
                start = popped[0]
            stack.append([start, h])

        for popped in stack:
            m = max(popped[1] * (len(heights) - popped[0]), m)
        return m      