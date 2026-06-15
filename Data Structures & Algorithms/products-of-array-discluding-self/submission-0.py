class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        prefix_left = [1] * (len(nums) + 1)
        prefix_right = [1] * (len(nums) + 1)

        for i, num in enumerate(nums):
            prefix_left[i+1] = num * prefix_left[i]

        for i in range(len(nums) - 1, -1, -1):
            prefix_right[i] = prefix_right[i + 1] * nums[i] 

        result = []
        for i in range(len(nums)):
            result.append(prefix_left[i] * prefix_right[i+1])

        return result
        