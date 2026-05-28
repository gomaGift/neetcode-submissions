class Solution:

    def findMin(self, nums: List[int]) -> int:

        left, right = 0, len(nums) - 1

        min_num = -1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > nums[-1]:
                left = mid + 1

            else:
                min_num = mid
                right = mid - 1

        return min_num


    def search(self, nums: List[int], target: int) -> int:
        min_idx = self.findMin(nums)

        low, right = 0, min_idx - 1
        while low <= right:
            mid = (low + right) // 2

            if nums[mid] == target:
                return mid

            if nums[mid] > target:
                right = mid -1

            else:
                low = mid + 1

        
        low, right = min_idx, len(nums) - 1
        while low <= right:
            mid = (low + right) // 2

            if nums[mid] == target:
                return mid

            if nums[mid] > target:
                right = mid -1

            else:
                low = mid + 1

        return -1
        
            
        