class Solution:
    def climbStairs(self, n: int) -> int:

        # what is dp[i]
        # what is the base case
        # how do i transition from dp[i-1] to dp[i]
        # what is my answer


        # top down technique the code is too innfiencice

        memo = {}
        def dp(stair_n):
        
            if stair_n <= 1:
                return 1

            if stair_n in memo:
                return memo[stair_n]
            
            ways_n = dp(stair_n - 1) + dp(stair_n - 2)
            memo[stair_n] = ways_n
            return ways_n

        return dp(n)
        