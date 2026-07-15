from typing import List
'''
Problem: Find The Original Array of Prefix Xor
Number: 70
Difficulty: Medium
Time Complexity: O(n)
Space Complexity: O(1)
URL: https://leetcode.com/problems/find-the-original-array-of-prefix-xor
Topics: Array, Bit Manipulation
'''
class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        if len(pref) < 2:
            return pref
        else:
            arr = [0]*len(pref)
            arr[0] = pref[0]
            for i in range(1,len(pref)):
                arr[i] = pref[i] ^ pref[i-1]
            return arr