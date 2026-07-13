class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        
        intervals.sort()
        res = []
        for query in queries:
            min_interval = float('inf')
            for start, end in intervals:
                if  start <= query and query <= end:
                    min_interval = min(min_interval, end - start + 1)
                elif start > query:
                    break

            min_interval = min_interval if min_interval != float('inf') else -1
            res.append(min_interval)

        return res