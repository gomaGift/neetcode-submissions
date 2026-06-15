class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:


        prefix_left = [1] * len(nums)
        prefix_right = [1] * len(nums)

        for i in range(1, len(nums)):
            prefix_left[i] = nums[i-1] * prefix_left[i - 1]

        for i in range(len(nums) - 2, -1, -1):
            prefix_right[i] = nums[i+1] * prefix_right[i + 1]

        
        result = []
        for i in range(len(nums)):
            result.append(prefix_left[i] * prefix_right[i])

        return result
        