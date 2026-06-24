class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        out = [-1] * len(nums1)

        nums2_map = {num:i for i, num in enumerate(nums2)}

        stack = []
        next_greater = [-1] * len(nums2)
        for i, num in enumerate(nums2):
            while stack and nums2[i] > nums2[stack[-1]]:
                idx = stack.pop()
                next_greater[idx] = nums2[i]
            stack.append(i)

        ans = [-1] * len(nums1)
        for i,num in enumerate(nums1):
            if num in nums2_map:
                ans[i] = next_greater[nums2_map[num]]

        return ans







        for i, num in enumerate(nums1):
            if num in nums2_map:
                idx = nums2_map[num]
                for j in range(idx + 1, len(nums2)):
                    if nums2[j] > nums1[i]:
                        out[i] = nums2[j]
                        break
                
                
        return out