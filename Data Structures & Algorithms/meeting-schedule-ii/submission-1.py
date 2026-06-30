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

        meetingRooms = []
        
        for interval in intervals:
            start = interval.start
            end = interval.end

            if not meetingRooms:
                meetingRooms.append([start,end])

            elif start < meetingRooms[-1][1]:
                meetingRooms.append([start,end])
        
        return len(meetingRooms)