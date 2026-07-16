from typing import List
'''
Problem: Remove Element
Number: 92
Difficulty: Easy
Time Complexity: O(n)
Space Complexity: O(1)
URL: https://leetcode.com/problems/remove-element
Topics: Array, Two Pointers
'''
class Solution:
    
    #Time Complexity: O(n²)
    #Space Complexity: O(1)
    def removeElement_1(self, nums: List[int], val: int) -> int:
        k = len([i for i in nums if i != val])
        while len(nums) > k:
            nums.remove(val)
        return k
    
    
    #Time Complexity: O(n)
    #Space Complexity: O(1)
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k
    
nums = [3,2,2,3]
s = Solution()
print(s.removeElement(nums,3))
print(nums)