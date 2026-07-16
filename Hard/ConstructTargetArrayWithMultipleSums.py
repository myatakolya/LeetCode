import heapq
from typing import List
'''
Problem: Construct Target Array With Multiple Sums
Number: 73
Difficulty: Hard
Time Complexity: O(n*log(n))
Space Complexity: O(n)
URL: https://leetcode.com/problems/construct-target-array-with-multiple-sums
Topics: Array, Heap, Math
'''
class Solution:
    def isPossible(self, target: List[int]) -> bool:
        total = sum(target)
        max_heap = [-x for x in target]
        heapq.heapify(max_heap)
        
        while True:
            max_val = -heapq.heappop(max_heap)
            if max_val == 1:
                return True
            rest = total - max_val
            if rest == 0 or rest >= max_val:
                return False
            new_val = max_val % rest
            if new_val == 0:
                if rest == 1:
                    return True
                return False
            total = total - max_val + new_val
            heapq.heappush(max_heap, -new_val)