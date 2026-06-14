class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

       if not nums:
        return 0
       look_up = set(nums)

       longest = 1
       for i, num in enumerate(nums):
           if num - 1 not in look_up:
              curr_seq = 1
              curr_num = num
              while curr_num + 1 in look_up:
                curr_seq += 1
                curr_num += 1
                longest = max(longest, curr_seq)
       return longest
