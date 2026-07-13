"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:

        ends = sorted([interval.end for interval in intervals])
        starts = sorted([interval.start for interval in intervals])

        rooms_need = 0
        end_index = 0
        for start in starts:
            if start < ends[end_index]:
                rooms_need += 1
            else:
                end_index += 1

        return rooms_need
            

       

        
        
    
      