class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        def merge_interval(interval1, interval2):
            new_start = min(interval1[0], interval2[0])
            new_end = max(interval1[1], interval2[1])

            return [new_start, new_end]

        
        def should_merge(interval1, interval2):
            return interval1[0] <= interval2[1] and interval2[0] <= interval1[1]

        intervals.sort(key=lambda x: x[0])

        res = [intervals[0]]
        for interval in intervals[1:]:
            if should_merge(res[-1], interval):
                merged = merge_interval(res[-1], interval)
                res[-1] = merged
            else:
                res.append(interval)

        return res

        