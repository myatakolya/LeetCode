from typing import List
'''
Problem: Concatenation of Array
Number: 30
Difficulty: Easy
Time Complexity: O(n)
Space Complexity: O(n)
URL: https://leetcode.com/problems/concatenation-of-array
Topics: Array, Simulation
'''
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        return nums*2
    
    def getConcatenation2(self, nums: List[int]) -> List[int]:
        return nums.extend(nums)
    
    def getConcatenation3(self, nums: List[int]) -> List[int]:
        return nums + nums

    def getConcatenation4(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            nums.append(nums[i])
        return nums
    
    #XD, сложно