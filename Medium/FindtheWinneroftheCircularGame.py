'''
Problem: Find the Winner of the Circular Game
Number: 16
Difficulty: Medium
Time Complexity: O(n)
Space Complexity: O(1)
URL: https://leetcode.com/problems/find-the-winner-of-the-circular-game
Topics: Math, Recursion, Simulation, Queue
'''

class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        pos = 0
        for i in range(2,n+1):
            pos = (pos+k) % i
        return pos + 1
            