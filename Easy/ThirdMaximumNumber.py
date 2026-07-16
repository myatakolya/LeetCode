from typing import List
import heapq
'''
Problem: Third Maximum Number
Number: 98
Difficulty: Easy
Time Complexity: O(n)
Space Complexity: O(n)
URL: https://leetcode.com/problems/third-maximum-number
Topics: Array, Sorting, Heap
'''
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        set_nums = [-i for i in set(nums)]
        heapq.heapify(set_nums)
        if len(set_nums) < 3:
            return -heapq.heappop(set_nums)
        else:
            _,_,t = heapq.heappop(set_nums),heapq.heappop(set_nums),-heapq.heappop(set_nums)
            return t
