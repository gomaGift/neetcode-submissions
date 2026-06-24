class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels_prefix_sum = [0] * (len(words) + 1)
        vowels = set(['a', 'e', 'i', 'o', 'u'])

        for i in range(1, len(vowels_prefix_sum)):
            word = words[i-1]
            vowels_prefix_sum[i] = vowels_prefix_sum[i-1] + 1 if (word[0] in vowels and word[-1] in vowels) else vowels_prefix_sum[i-1]

        out = []
        for left, right in queries:
            w_count = vowels_prefix_sum[right + 1] - vowels_prefix_sum[left]
            out.append(w_count)

        return out 

        