class Solution:
  def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
     



        left = 0
        q = deque()
        out = []
        for i, num in enumerate(nums):
            while q and nums[q[-1]] <= num:
                q.pop()

            q.append(i)

            if i - q[0] == k:
                q.popleft()


            if i - left + 1 == k:
                out.append(nums[q[0]])
                left += 1

        return out
          







        # output = []
        # curr_max = max(nums[:k])
        # output.append(curr_max)
       
        # for right in range(k, len(nums)):
        #     curr_max = sorted(nums[right - k+1:right+1])[-1]
        #     output.append(curr_max)

        # return output

        