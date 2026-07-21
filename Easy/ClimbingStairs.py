'''
Problem: Climbing Stairs
Number: 128
Difficulty: Easy
Time Complexity: O(n)
Space Complexity: O(1)
URL: https://leetcode.com/problems/climbing-stairs
Topics: Math, Dynamic Programming, Memoization
'''
class Solution:
    def climbStairs_1(self, n: int) -> int:
        prev_1 = 2
        prev_2 = 1
        if n == 1:
            return prev_2
        elif n == 2:
            return prev_1
        else:
            for _ in range(3,n+1):
                prev_1, prev_2 = prev_1 + prev_2, prev_1
        return prev_1


    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def climbStairs_Bine(self, n: int) -> int:
        fi = (1 + 5**0.5)/2
        ui = (1 - 5**0.5)/2
        res = int((fi**(n+1) - ui**(n+1))/5**0.5)
        return res
                