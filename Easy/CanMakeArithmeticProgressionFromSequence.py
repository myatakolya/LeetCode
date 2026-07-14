from typing import List
'''
Problem: Can Make Arithmetic Progression From Sequence
Number: 45
Difficulty: Easy
Time Complexity: O(n*log(n))
Space Complexity: O(1)
URL: https://leetcode.com/problems/can-make-arithmetic-progression-from-sequence
Topics: Array, Sorting, Math
'''
class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        step = arr[1] - arr[0]
        for i in range(len(arr)-1):
            if (arr[i+1] - arr[i]) != step:
                return False
        return True