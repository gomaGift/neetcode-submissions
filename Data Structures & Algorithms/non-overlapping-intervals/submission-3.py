class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        intervals.sort(key=lambda pair: pair[1])
        count = 0
        res = [intervals[0]]
        last_end = res[-1][1]

        for start, end in intervals[1:]:
            if start < last_end:
                count += 1
            else:
                last_end = end
        return count

        

        intervals.sort(key=lambda pair: pair[0])

        for start, end in intervals[1:]:
            if start < res[-1][1]:
                res[-1][1] = min(res[-1][1], end)
            else:
                res.append([start, end])

        return len(intervals) - len(res)

        