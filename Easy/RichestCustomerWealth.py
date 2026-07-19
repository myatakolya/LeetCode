from typing import List
'''
Problem: Richest Customer Wealth
Number: 114
Difficulty: Easy
Time Complexity: O(m*n)
Space Complexity: O(1)
URL: https://leetcode.com/problems/richest-customer-wealth
Topics: Array, Matrix
'''
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_summa = 0
        for money in accounts:
            cur_summa = 0
            while money:
                cur_summa += money.pop()
            max_summa = max(max_summa, cur_summa)
        return max_summa