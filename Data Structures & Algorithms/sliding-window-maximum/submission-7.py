class Solution:
  def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

    left = 0
    que = deque()
    output = []

    for right, num in enumerate(nums):
        if not que:
            que.append((num, right))

        elif num <= que[-1][0]:
            que.append((num, right))

        else:
            while que and num > que[-1][0]:
                que.pop()

            que.append((num, right))


        if right - left + 1 == k:
            while que[0][1] < left:
                que.popleft()

            output.append(que[0][0])
            left += 1
            
    return output

            

          










        # output = []
        # curr_max = max(nums[:k])
        # output.append(curr_max)
       
        # for right in range(k, len(nums)):
        #     curr_max = sorted(nums[right - k+1:right+1])[-1]
        #     output.append(curr_max)

        # return output

        