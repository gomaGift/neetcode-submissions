class Solution:
        
                    

    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        n = mountainArr.length() - 1
        left, right = 0, n
        peak = -1
        while left <= right:
            mid = (left + right) // 2
            if mid + 1 <= n:
                if mountainArr.get(mid) < mountainArr.get(mid + 1):
                    left = mid + 1
                else:
                    peak = mid
                    right = mid - 1
                    
            else:
                peak = mid
                break


        left, right = 0, peak
        ans1 = math.inf
        while left <= right:
            mid = (left + right) // 2
            if mountainArr.get(mid) == target:
                ans1 = mid
                break
            if mountainArr.get(mid) > target:
                right = mid -1
            else:
                left = mid + 1
        
        left, right = peak + 1, n
        ans2 = math.inf
        while left <= right:
            mid = (left + right) // 2
            if mountainArr.get(mid) == target:
                ans2 = mid
                break
            if mountainArr.get(mid) > target:
                left = mid  + 1
            else:
                right = mid - 1

        return -1 if min(ans1, ans2) == math.inf else min(ans1, ans2)
        


        

        

