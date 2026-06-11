class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        curr_max = max(nums[:k])
        output.append(curr_max)
       
        for right in range(k, len(nums)):
            curr_max = sorted(nums[right - k+1:right+1])[-1]
            output.append(curr_max)


        return output

        