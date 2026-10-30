class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        prev = 0
        c = Counter(nums)
        for i in range(3):
            for j in range(prev, prev + c[i]):
                nums[j] = i
            prev += c[i]
