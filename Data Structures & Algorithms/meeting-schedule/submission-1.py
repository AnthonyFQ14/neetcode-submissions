"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

        start = sorted([interval.start for interval in intervals])
        end = sorted([interval.end for interval in intervals])

        meetings = 0

        s, e = 0, 0

        while s < len(intervals):

            if start[s] < end[e]:
                meetings += 1
                s += 1
            else:
                meetings -= 1
                e += 1
            
            if meetings > 1:
                return False



        return True