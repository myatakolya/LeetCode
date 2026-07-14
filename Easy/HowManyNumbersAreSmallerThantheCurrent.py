from typing import List
from collections import Counter
'''
Problem: How Many Numbers Are Smaller Than the Current Number
Number: 34
Difficulty: Easy
Time Complexity: O(n*log(n))
Space Complexity: O(n)
URL: https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number
Topics: Array, Sorting, Hash Table
'''
class Solution:
    
    #Time Complexity: O(n²)
    #Space Complexity: O(n)
    def smallerNumbersThanCurrent2(self, nums: List[int]) -> List[int]:
        res = [0]*len(nums)
        slow,fast = 0,0
        while slow < len(nums):
            while fast < len(nums):
                if nums[fast] < nums[slow]:
                    res[slow] += 1
                fast += 1
            slow += 1
            fast = 0
        return res
    
    
    #Time Complexity: O(n*m)
    #Space Complexity: O(m)+O(n)
    def smallerNumbersThanCurrent1(self, nums: List[int]) -> List[int]:
        counter = Counter(nums)
        res = [0]*len(nums)
        for i in range(len(nums)):
            for j in counter:
                if j < nums[i]:
                    res[i] += counter[j]
        return res
    
    #Time Complexity: O(n*log(n))
    #Space Complexity: O(n)
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_nums = sorted(nums)
        first_index = {}
        for i in range(len(sorted_nums)):
            if sorted_nums[i] not in first_index:
                first_index[sorted_nums[i]] = i

        return [first_index[i] for i in nums]
    
s = Solution()
print(s.smallerNumbersThanCurrent([8,1,2,2,3]))