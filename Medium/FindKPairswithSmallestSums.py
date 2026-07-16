import heapq
from typing import List
'''
Problem: Find K Pairs with Smallest Sums
Number: 72
Difficulty: Medium
Time Complexity: O(n*log(n))
Space Complexity: O(n)
URL: https://leetcode.com/problems/find-k-pairs-with-smallest-sums
Topics: Array, Heap, Sorting
'''
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        if not nums1 or not nums2 or k == 0:
            return []
        
        heap = []
        for i in range(min(k, len(nums2))):
            heapq.heappush(heap, (nums1[0] + nums2[i], 0, i))
        
        res = []
        while heap and len(res) < k:
            _, i, j = heapq.heappop(heap)
            res.append([nums1[i], nums2[j]])
            if i + 1 < len(nums1):
                heapq.heappush(heap, (nums1[i+1] + nums2[j], i+1, j))
        return res