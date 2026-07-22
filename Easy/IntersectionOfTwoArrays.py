from typing import List
'''
Problem: Intersection of Two Arrays
Number: 120
Difficulty: Easy
Time Complexity: O(n+m)
Space Complexity: O(n+m)
URL: https://leetcode.com/problems/intersection-of-two-arrays
Topics: Array, Hash Table, Sorting, Two Pointers
'''
class Solution:
    #Time Complexity: O(n+m)
    #Space Complexity: O(n+m)
    def intersection_1(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        set_n1 = set(nums1)
        set_n2 = set(nums2)
        for i in set_n2:
            if i in set_n1:
                res.append(i)


    #Time Complexity: O(n*m)
    #Space Complexity: O(n)               
    def intersection_two_pointers(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = set()
        p1,p2 = 0,0
        n,m = len(nums1), len(nums2)
        while p1 < n:
            while p2 < m:
                if nums1[p1] == nums2[p2]:
                    res.add(nums1[p1])
                p2 += 1
            p1 += 1
            p2 = 0
        return list(res)
    
    #Time Complexity: O(n+m)
    #Space Complexity: O(n+m)
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1) & set(nums2))