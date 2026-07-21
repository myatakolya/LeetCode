from typing import List
'''
Problem: Best Time to Buy and Sell Stock
Number: 118
Difficulty: Easy
Time Complexity: O(n)
Space Complexity: O(1)
URL: https://leetcode.com/problems/best-time-to-buy-and-sell-stock
Topics: Array, Dynamic Programming, Greedy
'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_buy = float('inf')
        for i in prices:
            if i < min_buy:
                min_buy = i
            else:
                if i - min_buy > max_profit:
                    max_profit = i-min_buy
        return max_profit