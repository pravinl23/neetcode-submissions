class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x : x[1])
        end = intervals[0][1]
        cut = 0

        for i in intervals:
            if i[0] < end:
                cut += 1
            else:
                end = i[1]

        return cut -1 