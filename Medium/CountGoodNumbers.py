'''
Problem: Count Good Numbers
Number: 17
Difficulty: Medium
Time Complexity: O(log n)
Space Complexity: O(1)
URL: https://leetcode.com/problems/count-good-numbers
Topics: Math, Recursion, Exponentiation
'''
class Solution:
    def countGoodNumbers(self, n: int) -> int:
        even = (n+1)//2
        odd = n//2
        MOD = 10**9 + 7
        return (pow(5,even,MOD) * pow(4,odd,MOD)) % MOD
    
