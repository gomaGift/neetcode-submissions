class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        ans = []
        for num in nums:
            heapq.heappush(ans, num)
            if len(ans) > k:
                heapq.heappop(ans)

        return ans[0]
        