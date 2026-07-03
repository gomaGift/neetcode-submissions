class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mono_stack = []
        max_profit = 0
        for num in prices:
           
            while mono_stack and num <= mono_stack[-1]:
                mono_stack.pop()
            
            mono_stack.append(num)
            
            if mono_stack:
                max_profit = max(max_profit, mono_stack[-1] - mono_stack[0])
        return max_profit
