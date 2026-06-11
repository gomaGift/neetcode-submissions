class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need_map = Counter(t)
        need = len(need_map)
        s_map = {}
        have = 0
        output = ""
        output_len = math.inf
        left = 0

        for right, char in enumerate(s):
            s_map[char] = s_map.get(char, 0) + 1

            if char in need_map and s_map[char] == need_map[char]:
                have += 1

            while have == need:
                if right - left + 1 < output_len:
                    output_len = right-left+1
                    output = s[left:right+1]
                
                s_map[s[left]] -= 1
                if s[left] in need_map and s_map[s[left]] < need_map[s[left]]:
                    have -= 1
                left += 1

        return output



        