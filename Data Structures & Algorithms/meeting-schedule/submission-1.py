"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda x: x.start)
        for i,interv in enumerate(intervals):
            if i==0:
                continue
            print(intervals[i-1].end, intervals[i].start)
            if intervals[i-1].end > intervals[i].start:
                return False
        return True