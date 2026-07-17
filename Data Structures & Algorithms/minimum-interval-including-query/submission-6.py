from collections import deque
class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        
        intervals.sort()
        
        res = [-1] * len(queries)
        query_map = defaultdict(deque)
        for i, val in enumerate(queries):
            query_map[val].append(i)

        queries = sorted(queries)
        print(queries)
        heap = []
        i = j = 0
        while i < len(intervals) or j < len(queries):    

            query = queries[j]

        
            while i < len(intervals) and query >= intervals[i][0]:
                heapq.heappush(heap, (intervals[i][1] - intervals[i][0] + 1, intervals[i][1]))
                i += 1

            while heap and query > heap[0][1]:
                heapq.heappop(heap)
           

            if heap:
                idx_q = query_map[query]
                idx = idx_q.popleft()
                res[idx] = heap[0][0]


            if j + 1 == len(queries):
                break
            j+=1
        return res
            


            
