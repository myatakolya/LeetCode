from typing import List
'''
Problem: Build an Array With Stack Operations
Number: 39
Difficulty: Easy
Time Complexity: O(n)
Space Complexity: O(n)
URL: https://leetcode.com/problems/build-an-array-with-stack-operations
Topics: Array, Stack, Simulation
'''
class Solution:

    #Time Complexity: O(n)
    #Space Complexity: O(n)
    def buildArray(self, target: List[int], n: int) -> List[str]:
        uniq = set(target)
        stack = []
        res = []
        for i in range(1,n+1):
            if len(stack) == len(target):
                return res
            elif i in uniq:
                stack.append(i)
                res.append('Push')
            elif i not in uniq:
                res.append('Push')
                res.append('Pop')
        return res
    
    #Time Complexity: O(len(target))
    #Space Complexity: O(len(res))
    
    def buildArray_2(self, target: List[int], n: int) -> List[str]:
        res = []
        current = 1
        
        for num in target:
            while current < num:
                res.append('Push')
                res.append('Pop')
                current += 1
            res.append('Push')
            current += 1
        return res
