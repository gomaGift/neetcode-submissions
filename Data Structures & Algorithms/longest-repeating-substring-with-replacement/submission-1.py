
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #  this is an on application
        # first replace then find distinct
        counter = {}
        left = 0
        output = 0

        max_freq = 0
        for right, char in enumerate(s):
            counter[char] = counter.get(char, 0) + 1
            max_freq = max(counter[char], max_freq)
            print(counter)
            while (right - left + 1) - max_freq > k:
                counter[s[left]] -= 1
                left += 1
            output = max(right - left  + 1, output)


        return output



        