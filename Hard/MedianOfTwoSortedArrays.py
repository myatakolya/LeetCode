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
#For findMedianSortedArraysBIN Time Complexity: O(log min(m,n)) and Space Complexity: O(1)
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums3 = sorted(nums1 + nums2)
        lenght = len(nums3)
        half = lenght//2
        if lenght % 2 != 0:
            return nums3[half]
        else:
            return (nums3[half] + nums3[half-1])/2
    
    def findMedianSortedArraysBIN(self, nums1: List[int], nums2: List[int]) -> float:
        n1 = len(nums1)
        n2 = len(nums2)
        
        if n1 > n2:
            return self.findMedianSortedArraysBIN(nums2, nums1)
        
        n = n1 + n2
        left = (n1 + n2 + 1) // 2
        low = 0
        high = n1
        
        while low <= high:
            mid1 = (low + high) // 2
            mid2 = left - mid1
            
            l1 = float('-inf')
            l2 = float('-inf')
            r1 = float('inf')
            r2 = float('inf')
            
            if mid1 < n1:
                r1 = nums1[mid1]
            if mid2 < n2:
                r2 = nums2[mid2]
            if mid1 - 1 >= 0:
                l1 = nums1[mid1 - 1]
            if mid2 - 1 >= 0:
                l2 = nums2[mid2 - 1]
            
            if l1 <= r2 and l2 <= r1:
                if n % 2 == 1:
                    return max(l1, l2)
                else:
                    return (max(l1, l2) + min(r1, r2)) / 2.0
            elif l1 > r2:
                high = mid1 - 1
            else:
                low = mid1 + 1
        
        return 0
        
nums1 = [1,3]
nums2 = [2]
nums3 = [1,2]
nums4 = [3,4]
solver = Solution()
print(solver.findMedianSortedArrays(nums1,nums2))
print(solver.findMedianSortedArrays(nums3,nums4))
print(solver.findMedianSortedArraysBIN(nums1,nums2))
print(solver.findMedianSortedArraysBIN(nums3,nums4))
