from typing import List
'''
Problem: Single Number
Number: 26
Difficulty: Easy
Time Complexity: O(n)
Space Complexity: O(1)
URL: https://leetcode.com/problems/single-number
Topics: Array, Bit Manipulation
'''
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for i in nums:
            res = res ^ i
        return res
            
                

n1 = [2,2,1]
n2 =[4,1,2,1,2]
n3 = [1]
s = Solution()
print(s.singleNumber(n1))
print(s.singleNumber(n2))
print(s.singleNumber(n3))