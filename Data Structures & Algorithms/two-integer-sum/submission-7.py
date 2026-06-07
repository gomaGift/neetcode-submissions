class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        used = {nums[0]: 0}
        for i in range(1, len(nums)):
            num_target_sum = target - nums[i]
            if num_target_sum in used:
                return [used[num_target_sum], i]

            used[nums[i]] = i
