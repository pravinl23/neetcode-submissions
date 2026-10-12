class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        m = 0
        while l < r:
            total = min(heights[l], heights[r]) * (r - l)
            m = max(m, total)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return m