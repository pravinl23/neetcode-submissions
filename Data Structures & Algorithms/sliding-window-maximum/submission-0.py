from collections import defaultdict
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        nums = [-x for x in nums]
        heap = []
        toppop = {}
        for n in nums:
            if n not in toppop:
                toppop[n] = 0
        l, r = 0, 0
        res = []
        while r < len(nums) and l < (len(nums) - k + 1):
            while (r - l + 1) <= k:
                heapq.heappush(heap, nums[r])
                r += 1
            while toppop[heap[0]] != 0:
                toppop[heapq.heappop(heap)] -= 1
                
            res.append(-(heap[0]))

            toppop[nums[l]] += 1
            l += 1

        return res





