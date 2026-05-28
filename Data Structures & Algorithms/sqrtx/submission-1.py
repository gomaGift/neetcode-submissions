class Solution:
    def mySqrt(self, x: int) -> int:

        possible_root = 0

        left, right = 1, x

        while left <= right:
            mid = (left + right) // 2
            square = mid * mid
            if square == x:
                return mid

            if square < x:
                possible_root = mid
                left = mid + 1
            else:
                right = mid -1

        return possible_root
                
        