from typing import List
'''
Problem: Sign of the Product of an Array
Number: 107
Difficulty: Easy
Time Complexity: O(n)
Space Complexity: O(1)
URL: https://leetcode.com/problems/sign-of-the-product-of-an-array
Topics: Array, Math
'''
class Solution:
       
    def arraySign(self, nums: List[int]) -> int:
        negativ = 0
        for i in nums:
            if i == 0:
                return 0
            elif i < 0:
                negativ += 1
        
        if negativ % 2 == 0:
            return 1
        return -1
        