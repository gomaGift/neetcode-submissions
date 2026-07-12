class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        required = 0

        intervals.sort(key=lambda pair: pair[0])
        res = [intervals[0]]

        for start, end in intervals[1:]:
            if start < res[-1][1]:
                res[-1][1] = min(res[-1][1], end)
            else:
                res.append([start, end])

        return len(intervals) - len(res)

        