class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        if not intervals:
            return [newInterval]

        inserted = False
        
        res = []

        if newInterval[0] <= intervals[0][0]:
            res = [newInterval]
            inserted = True
        else:
            res = [intervals[0]]

        print(res)
        for start, end in intervals:
            if not inserted:
                if newInterval[0] <= res[-1][1]:
                    res[-1] = [min(newInterval[0], res[-1][0]), max(newInterval[1], res[-1][1])]
                    inserted = True
                elif newInterval[1] <= start:
                    res.append(newInterval)
                    inserted = True

            if start <= res[-1][1]:
                res[-1][1] = max(res[-1][1], end)
            else:
                res.append([start, end])
        if not inserted:
            res.append(newInterval)
        return res