class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        prev_stack = []
        next_stack = []
        prev_smaller = [-1] * len(heights)
        next_smaller = [-1] * len(heights)
        for i, num in enumerate(heights):
            while prev_stack and heights[prev_stack[-1]] >= num:
                prev_stack.pop()

            if prev_stack:
                prev_smaller[i] = prev_stack[-1]

            prev_stack.append(i)

            while next_stack and num < heights[next_stack[-1]]:
                idx = next_stack.pop()
                next_smaller[idx] = i

            next_stack.append(i)


        area = -math.inf
        n = len(heights)
        for i, num in enumerate(heights):
            prev_i = prev_smaller[i]
            next_i = next_smaller[i]

            if prev_i == -1 and next_i == -1:
                area = max(area, num * n)

            elif prev_i != -1 and next_i != -1:
                area = max(area, num * (next_i - prev_i - 1))

            elif prev_i == -1:
                area = max(area, num * next_i)

            else:
                area = max(area, num * (n - 1 - prev_i))

        return area