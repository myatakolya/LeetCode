from typing import List
'''
Problem: Counting Bits
Number: 91
Difficulty: Easy
Time Complexity: O(n)
Space Complexity: O(n)
URL: https://leetcode.com/problems/counting-bits
Topics: Array, Dynamic Programming, Bit Manipulation
'''
class Solution:
    def countBits(self, n: int) -> List[int]:
        arr = [0] * (n+1)
        for i in range(1,len(arr)):
            arr[i] = arr[i >> 1] + (i & 1)
        return arr