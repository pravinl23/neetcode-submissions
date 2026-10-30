class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = set()
        l = 0
        r = 0
        while r < len(nums) and (r - l) < k:
            if nums[r] in seen:
                return True
            seen.add(nums[r])
            r += 1

        while r < len(nums):
            if nums[r] in seen:
                return True
            seen.add(nums[r])
            r += 1
            seen.remove(nums[l])
            l += 1

        return False
            