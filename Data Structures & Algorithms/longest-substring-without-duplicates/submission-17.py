class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if not s:
            return 0

        left = 0
       
        seen = {}
        max_len = 0
        for right, char in enumerate(s):
            if char in seen and seen[char] >= left:
                left = seen[char] + 1
            
            max_len = max(max_len, right - left + 1)
            seen[char] = right



        return max_len
        