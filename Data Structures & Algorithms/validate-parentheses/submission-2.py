class Solution:
    def isValid(self, s: str) -> bool:
        pair = {'(':')', '{':'}', '[': ']'}

        stack = []

        for char in s:
            if char in pair:
                stack.append(char)

            else:
                if not stack or pair [stack[-1]] != char:
                    return False
                stack.pop()
                    

            

        return not stack


        