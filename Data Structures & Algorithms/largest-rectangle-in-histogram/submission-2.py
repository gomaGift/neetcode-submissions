class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        increasing_stack = []
        area = -math.inf
        for i, num in enumerate(heights):
            prev_small_i = i
            while increasing_stack and num < increasing_stack[-1][1]:
                prev_small_i, height = increasing_stack.pop()
                area = max(area, height * (i - prev_small_i))
            increasing_stack.append((prev_small_i, num))

        while increasing_stack:
                prev_small, height = increasing_stack.pop()
                area = max(area, height * (len(heights) - prev_small))

        return area
                
        

