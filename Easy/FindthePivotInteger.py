'''
Problem: Find the Pivot Integer
Number: 48
Difficulty: Easy
Time Complexity: O(n)
Space Complexity: O(1)
URL: https://leetcode.com/problems/find-the-pivot-integer
Topics: Math, Prefix Sum
'''
class Solution:
    def pivotInteger(self, n: int) -> int:
        if n == 1:
            return 1
        else:
            for x in range(1,n+1):
                from_1_to_n = (n*(n+1))//2
                from_1_to_x = (x*(x+1))//2
                if from_1_to_x == (from_1_to_n - from_1_to_x + x):
                    return x
        return -1