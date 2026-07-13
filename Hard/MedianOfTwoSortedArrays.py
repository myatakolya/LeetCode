from typing import List
'''
Problem: Median of Two Sorted Arrays
Number: 2
Difficulty: Hard
Time Complexity: O((m+n) log(m+n))
Space Complexity: O(m+n)
URL: https://leetcode.com/problems/median-of-two-sorted-arrays
Topics: Array, Binary Search, Divide and Conquer
''' 

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums3 = sorted(nums1 + nums2)
        lenght = len(nums3)
        half = lenght//2
        if lenght % 2 != 0:
            return nums3[half]
        else:
            return (nums3[half] + nums3[half-1])/2
        
nums1 = [1,3]
nums2 = [2]
nums3 = [1,2]
nums4 = [3,4]
solver = Solution()
print(solver.findMedianSortedArrays(nums1,nums2))
print(solver.findMedianSortedArrays(nums3,nums4))
print(solver.findMedianSortedArraysBIN(nums1,nums2))
print(solver.findMedianSortedArraysBIN(nums3,nums4))
