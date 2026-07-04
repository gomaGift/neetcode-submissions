class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]
            
        
        

        nums_with_first = nums[:len(nums) - 1]
        
        rob1_with_first = rob2_with_first = 0
        for num in nums_with_first:
            temp = max(num + rob1_with_first, rob2_with_first)
            rob1_with_first = rob2_with_first
            rob2_with_first = temp


        nums_without_first = nums[1:]
        rob1_without_first = rob2_without_first = 0
        for num in nums_without_first:
            temp = max(num + rob1_without_first, rob2_without_first)
            rob1_without_first = rob2_without_first
            rob2_without_first = temp

        return max(rob2_with_first, rob2_without_first)


        
