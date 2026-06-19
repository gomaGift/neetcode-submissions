class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        area = 0

        while left < len(height) - 1:
            right = curr_index = left + 1
            while right < len(height) and height[right] < height[left]:
                right += 1
                
            while right < len(height) and curr_index < right:
                area += min(height[left], height[right]) - height[curr_index]
                curr_index += 1

            if right == len(height):
                 while curr_index < len(height) and height[curr_index] < height[-1]:
                    area += min(height[left], height[-1]) - height[curr_index]
                    curr_index += 1

            

            left = curr_index

        return area
        