class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        
        curr = [0,0,0]
        for t in triplets:
            if t[0] == target[0] and t[1] <= target[1] and t[2] <= target[2]:
                curr[0] = t[0]
            if t[1] == target[1] and t[0] <= target[0] and t[2] <= target[2]:
                curr[1] = t[1]
            if t[2] == target[2] and t[1] <= target[1] and t[0] <= target[0]:
                curr[2] = t[2]
        
        for c in curr:
            if c == 0:
                return False
        return True