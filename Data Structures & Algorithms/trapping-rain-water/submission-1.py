class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        l_height, r_height = height[l], height[r]
        rain = 0
        while l < r:
            if l_height <= r_height:
                l += 1
            else:
                r -= 1
            l_height = max(l_height, height[l])
            r_height = max(r_height, height[r])
            rain += l_height - height[l]
            rain += r_height - height[r]

        return rain

