class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefixProduct = [1] * n
        suffixProduct = [1] * n

        running = 1
        for i in range(0, n - 1):
            running *= nums[i]
            prefixProduct[i + 1] = running
        running = 1
        for i in range(n - 1, 0, -1):
            running *= nums[i]
            suffixProduct[i - 1] = running

        res = []
        for i in range(n):
            res.append(prefixProduct[i] * suffixProduct[i])

        return res


        
        