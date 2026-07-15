from typing import List
import heapq
'''
Problem: Last Stone Weight
Number: 71
Difficulty: Easy
Time Complexity: O(n*log(n))
Space Complexity: O(n)
URL: https://leetcode.com/problems/last-stone-weight
Topics: Array, Heap, Simulation
'''
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] = -stones[i]
        heapq.heapify(stones)
        while stones:
            if len(stones) == 1:
                return -heapq.heappop(stones)
            y = heapq.heappop(stones)
            x = heapq.heappop(stones)
            if x != y:
                heapq.heappush(stones, -(abs(y)-abs(x)))
        return 0
        
s = Solution()
print(s.lastStoneWeight([1,1,1]))   
        