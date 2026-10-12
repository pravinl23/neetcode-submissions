class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {} # need : num
        for i, n in enumerate(nums):
            need = target - n
            if n in seen:
                return [seen[n], i]
            seen[need] = i

