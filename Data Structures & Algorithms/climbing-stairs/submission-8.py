class Solution:
    def climbStairs(self, n: int) -> int:

        # what is dp[i]
        # what is the base case
        # how do i transition from dp[i-1] to dp[i]
        # what is my answer
        
        # Bottom up approach 
        # what is dp[i] number of ways to reach step i

        dp = [0] * (n+1)
        dp[0] = dp[1] = 1

        for i in range(2, n + 1):
            dp[i] = dp[i-1] + dp[i-2]

        return dp[n]
        



























        # top down technique the code is too innfiencice

        memo = {}
        def top_down_dp(stair_n):
        
            if stair_n <= 1:
                return 1

            if stair_n in memo:
                return memo[stair_n]
            
            ways_n = top_down_dp(stair_n - 1) + top_down_dp(stair_n - 2)
            memo[stair_n] = ways_n
            return ways_n

        return top_down_dp(n)
        