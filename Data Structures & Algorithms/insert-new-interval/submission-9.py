class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        if not intervals:
            return [newInterval]

        res = []

        new_start, new_end = newInterval
 
        for i, (start, end) in enumerate(intervals):
           # case 1 current interval happens before new interval`
            if end < new_start:
              res.append([start, end])

            # case 2 new interval happens before the current interval 
            elif new_end < start:
                 res.append([new_start, new_end])
                 return res + intervals[i:]

            # new interval overlaps with current interval
            else:
                new_start = min(start, new_start)
                new_end = max(end, new_end)


        res.append([new_start, new_end])
        return res
        
     
        