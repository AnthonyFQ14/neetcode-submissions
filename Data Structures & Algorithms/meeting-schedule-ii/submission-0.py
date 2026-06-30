"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

# assertions
# stack with meeting times
# if end of sorted intervals of previous is after current

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        
        for interval in intervals:
            print(interval.start, interval.end)
        
        return 0