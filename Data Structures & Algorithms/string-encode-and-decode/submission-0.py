class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for string in strs:
            res.append(str(len(string)))
            res.append("#")
            res.append(string)
        s = ''.join(res)
        print(s)
        return s

    def decode(self, s: str) -> List[str]:
        res = []        
        i = j = 0

        while i < len(s):
            while s[i] != "#":
                i += 1

            word_len = int(s[j:i])
            j = i + 1
            i = j + word_len
            word = s[j: i]
            res.append(word)
            j = i

        return res


        
