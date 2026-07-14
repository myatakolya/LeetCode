from typing import List
from collections import Counter
'''
Problem: Find All Numbers Disappeared in an Array
Number: 36
Difficulty: Easy
Time Complexity: O(n)
Space Complexity: O(1)
URL: https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array
Topics: Array, Hash Table (in-place marking)
'''
class Solution:
    
    #Time Complexity: O(n)
    #Space Complexity: O(n) (из-за Counter)
    def findDisappearedNumbers_2(self, nums: List[int]) -> List[int]:
        seen = Counter(nums)
        res = []
        for i in range(1,len(nums)+1):
            if i not in seen:
                res.append(i)
        return res

    #Time Complexity: O(n)
    #Space Complexity: O(n) (из-за seen)
    def findDisappearedNumbers_1(self, nums: List[int]) -> List[int]:
        n = len(nums)
        seen = [False] * (n+1)
        for i in nums:
            seen[i] = True
            
        return [i for i in range(1,n+1) if seen[i] == False]


    #Time Complexity: O(n)
    #Space Complexity: O(1)
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(n):
            idx = abs(nums[i])-1
            if nums[idx] > 0:
                nums[idx] = -nums[idx]
        
        res = []
        for i in range(n):
            if nums[i] > 0:
                res.append(i+1)
        return res
        
s = Solution()
print(s.findDisappearedNumbers([4,3,2,7,8,2,3,1]))
print(s.findDisappearedNumbers_1([4,3,2,7,8,2,3,1]))
print(s.findDisappearedNumbers_2([4,3,2,7,8,2,3,1]))
        