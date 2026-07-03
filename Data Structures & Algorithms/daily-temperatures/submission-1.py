class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # pattern: next greater
        # monotonic stack: decreasing

        stack = []
        res = [0] * len(temperatures)
        for i, temp in enumerate(temperatures):

            while stack and temp > temperatures[stack[-1]]:
                idx = stack.pop()
                res[idx] = i - idx

            stack.append(i)

        return res