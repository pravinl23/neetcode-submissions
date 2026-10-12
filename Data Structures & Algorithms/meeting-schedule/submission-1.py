"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda x : x.start)
        for index in range(1, len(intervals)):
            if intervals[index - 1].end > intervals[index].start:
                return False

        return True