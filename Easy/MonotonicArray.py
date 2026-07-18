from typing import List
'''
Problem: Monotonic Array
Number: 103
Difficulty: Easy
Time Complexity: O(n)
Space Complexity: O(1)
URL: https://leetcode.com/problems/monotonic-array
Topics: Array
'''
class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return True
        increasing_monotonic = False
        decreasing_monotonic = False
        for i in range(1,len(nums)):
            if nums[i] > nums[i-1]:
                increasing_monotonic = True
            elif nums[i] < nums[i-1]:
                decreasing_monotonic = True
        
        return not (increasing_monotonic and decreasing_monotonic)
    
s = Solution()
n1 = [1,2,2,3]
n2 = [6,5,4,4]
n3 = [1,3,2]
n4 = [0]
print(s.isMonotonic(n1))
print(s.isMonotonic(n2))
print(s.isMonotonic(n3))
print(s.isMonotonic(n4))
        
        