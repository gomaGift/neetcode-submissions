import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # basically i need to find the distance and create a min heap that shoue
        # im heapifying by the distance and 

        ans = []
        for x, y in points:
            d_origin = math.sqrt(x**2 + y**2)
            heapq.heappush(ans, (d_origin, [x, y]))
        
        out = []
        for i in range(k):
            out.append(heapq.heappop(ans)[1])

        return out

