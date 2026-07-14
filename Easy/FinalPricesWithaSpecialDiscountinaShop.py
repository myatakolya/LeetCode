from typing import List
'''
Problem: Final Prices With a Special Discount in a Shop
Number: 42
Difficulty: Easy
Time Complexity: O(n)
Space Complexity: O(n)
URL: https://leetcode.com/problems/final-prices-with-a-special-discount-in-a-shop
Topics: Array, Stack, Monotonic Stack
'''
class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        res = [i for i in prices]
        monotonic_stack = []
        
        for i in range(len(prices)-1,-1,-1):
            
            while monotonic_stack and prices[monotonic_stack[-1]] > prices[i]:
                monotonic_stack.pop()
            
            if monotonic_stack:
                res[i] = prices[i] - prices[monotonic_stack[-1]]
        
            monotonic_stack.append(i) 
            
        return res