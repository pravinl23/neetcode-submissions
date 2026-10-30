class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        n = len(gas)
        
        g = 0
        starting = 0
        for i in range(n * 2):
            if i - starting == n:
                return starting
            i = i % n
            if gas[i] + g < cost[i]:
                g = 0
                starting = (i + 1) % n
                continue
            g += gas[i]
            g -= cost[i]

        return starting
            