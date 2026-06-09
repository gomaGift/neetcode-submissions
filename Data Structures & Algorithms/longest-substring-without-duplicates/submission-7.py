class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        
        left = 0
        char_map = {}
        length = 0
 
        for right, char in enumerate(s):
            if char in char_map and char_map[char] >= left:
                left = char_map[char] + 1

            length = max(length, right - left + 1)
            char_map[char] = right
        
        return length

        