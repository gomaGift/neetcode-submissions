class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        out = [-1] * len(nums1)

        nums2_map = {num:i for i, num in enumerate(nums2)}

        for i, num in enumerate(nums1):
            if num in nums2_map:
                idx = nums2_map[num]
                for j in range(idx + 1, len(nums2)):
                    if nums2[j] > nums1[i]:
                        out[i] = nums2[j]
                        break
                
                
        return out