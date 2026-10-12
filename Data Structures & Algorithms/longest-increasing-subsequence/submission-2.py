class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        ans = []
        ans.append(nums[0])

        for n in nums:
            if n > ans[-1]:
                ans.append(n)
                continue

            l, h = 0, len(ans) - 1
            replace = -1
            while l <= h:
                m = (l + h) // 2
                if ans[m] >= n:
                    replace = m
                    h = m - 1
                elif ans[m] < n:
                    l = m + 1
            ans[replace] = n

        return len(ans)

            
        