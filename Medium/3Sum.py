'''
Problem: 3Sum
Number: 3
Difficulty: Medium
Time Complexity: O(n²)
Space Complexity: O(1)
URL: https://leetcode.com/problems/3sum
Topics: Array, Two Pointers, Sorting
'''
from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[list[int]]:
        nums.sort()
        n = len(nums)
        res = []
        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue
        
            left = i+1
            right = n-1
            
            while left < right:
                summa = nums[i] + nums[left] + nums[right]
                    
                if summa < 0:
                    left += 1
                elif summa > 0:
                    right -= 1
                else:
                    res.append([nums[i],nums[left],nums[right]])
                
                while left < right and nums[left] == nums[left+1]:
                    left += 1
                
                while left < right and nums[right] == nums[right-1]:
                    right -= 1
                
                
                left += 1
                right -= 1
                
        return res
    
i1 = [-1,0,1,2,-1,-4] #[-4,-1,-1,0,1,2]
i2 = [0,1,1]
i3 = [0,0,0]
solver = Solution()
print(solver.threeSum(i1))
print(solver.threeSum(i2))
print(solver.threeSum(i3))
