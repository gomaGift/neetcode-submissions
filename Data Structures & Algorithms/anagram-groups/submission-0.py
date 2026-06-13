class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res_map = defaultdict(list)

        for i, word in enumerate(strs):
            alpha = [0] * 26

            for char in word:
                index = ord(char) - ord('a')
                alpha[index] += 1

            key = str(alpha)
            res_map[key].append(word)

        return list(res_map.values())