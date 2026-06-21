class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        
        nums3 = sorted(nums1 + nums2)

        if len(nums3) % 2:
            return float(nums3[len(nums3) // 2])

        return (nums3[len(nums3)//2] + nums3[len(nums3) // 2 - 1]) / 2.0 
        

        