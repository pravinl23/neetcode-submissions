class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        res = []
        for index, i in enumerate(intervals):
            if i[1] < newInterval[0]:
                res.append(i)
            elif i[0] > newInterval[1]:
                res.append(newInterval)
                return res + intervals[index:]
            else:
                newInterval[0] = min(i[0], newInterval[0])
                newInterval[1] = max(i[1], newInterval[1])

        res.append(newInterval)    
        return res
            
