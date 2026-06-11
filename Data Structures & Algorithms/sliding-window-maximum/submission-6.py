class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:


        max_stack = []
        temp_stack = []
        output = []
        left = 0
        for right, num in enumerate(nums):
            if not max_stack:
                max_stack.append((num, right))

            elif num > max_stack[-1][0]:
                max_stack.append((num, right))

            else:   
                while max_stack and num < max_stack[-1][0]:
                    temp_stack.append(max_stack.pop())

                max_stack.append((num, right))

                while temp_stack:
                    max_stack.append(temp_stack.pop())


            if right - left + 1 == k:
                while max_stack and max_stack[-1][1] < left:
                    max_stack.pop()

                output.append(max_stack[-1][0])
                left += 1

        return output

            

          










        # output = []
        # curr_max = max(nums[:k])
        # output.append(curr_max)
       
        # for right in range(k, len(nums)):
        #     curr_max = sorted(nums[right - k+1:right+1])[-1]
        #     output.append(curr_max)

        # return output

        