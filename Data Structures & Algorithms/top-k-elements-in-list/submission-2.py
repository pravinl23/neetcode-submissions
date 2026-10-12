class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        for i in range(1, len(nums) + 1):
            hashmap[i] = []
        countermap = {}
        for num in nums:
            countermap[num] = 1 + countermap.get(num, 0)
            hashmap[countermap[num]].append(num)
            if countermap[num] >= 2:
                hashmap[countermap[num] - 1].remove(num)
            
        ans = []
        for i in range(len(nums), 0, -1):
            if k == 0:
                return ans
            if len(hashmap[i]) >= 1:
                for num in (hashmap[i]):
                    ans.append(num)
                    k = k - 1
        return ans
