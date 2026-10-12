class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seek = {}
        for i, n in enumerate(nums):
            need = target - n
            if need in seek:
                return [seek[need], i]
            
            seek[n] = i

        