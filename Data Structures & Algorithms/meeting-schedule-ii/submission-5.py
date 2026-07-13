"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        
      
        events = []
        for interval in intervals:
            events.append((interval.start, 1))
            events.append((interval.end, -1))

        events.sort()


        current_rooms = 0
        rooms_required = 0
        for _, event_type in events:
            current_rooms += event_type
            rooms_required = max(current_rooms, rooms_required)

        return rooms_required