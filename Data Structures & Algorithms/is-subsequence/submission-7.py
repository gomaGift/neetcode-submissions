class Solution:
 def isSubsequence(self, s: str, t: str) -> bool:
    if not s:
        return True

    left = 0
    right = 0
    while right < len(t):
        while right < len(t) and left < len(s) and t[right] != s[left]:
            right += 1

        
        left += 1
        right += 1
        if left == len(s):
            break

    return left == len(s)


          

        