class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

       seen = set()
       longest = 0
       look_up = set(nums)
       for num in nums:
         if num - 1 not in seen:
            curr_num = num
            seq = 1

            while curr_num + 1 in look_up:
                seq += 1
                curr_num += 1
            longest = max(longest, seq)

         seen.add(num)

       return longest

       