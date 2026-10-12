class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        m = 0

        for n in nums:
            if n in s:
                curr = 1
                i = n + 1
                while i in s:
                    curr += 1
                    s.remove(i)
                    i += 1
                i = n - 1
                while i in s:
                    curr += 1
                    s.remove(i)
                    i -= 1
                m = max(m, curr)



        return m