class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        output = set()
        for i in range(len(nums) - 2):
            j = i + 1
            k = len(nums) - 1

            while j < k:
                if nums[j] + nums[k] + nums[i] == 0:
                    output.add((nums[i], nums[j], nums[k]))
                    k -= 1
                    
                elif nums[j] + nums[k] + nums[i] > 0:
                    k -= 1

                else:
                    j += 1

        return list(output)



                 