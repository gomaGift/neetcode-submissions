class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        permutation = [0] * 26
        for char in s1:
            permutation[ord(char) - ord('a')] += 1

        permutation = str(permutation)
        s1_len = len(s1)
        left = 0
       
        for right, char in enumerate(s2[s1_len - 1:], start=s1_len-1):
            freq = [0] * 26

            for j, c in enumerate(s2[left:right+1]):
                freq[ord(c) - ord('a')] += 1

            if permutation == str(freq):
                return True

            left += 1

        return False
            
            





        freq = Counter(s1)
        need = len(freq)
        have = 0

        s1_len = len(s1)
        
        char_map = {}
        left = 0
        for right, char in enumerate(s2):
            char_map[char] = char_map.get(char, 0) + 1

            if char in freq and char_map[char] == freq[char]:
                have += 1

            while have == need:
                if right - left + 1 == s1_len:
                   return True

                left_char = s2[left]
                char_map[left_char] -= 1
                if left_char in freq and char_map[left_char] < freq[left_char]:
                    have -= 1

                left += 1


        return False

