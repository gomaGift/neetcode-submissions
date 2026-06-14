class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

       
       look_up = set(nums)
       longest = 0

       for num in nums:
           if num - 1 not in look_up:
              curr_seq = 1
              curr_num = num
              while curr_num + 1 in look_up:
                curr_seq += 1
                curr_num += 1
              longest = max(longest, curr_seq)
       return longest
