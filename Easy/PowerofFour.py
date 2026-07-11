'''
Problem: Power of Four
Number: 7
Difficulty: Easy
Time Complexity: O(1)
Space Complexity: O(1)
URL: https://leetcode.com/problems/power-of-four
Topics: Math, Bit Manipulation
'''
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return (n > 0) and (n & (n-1) == 0) and (n % 3 == 1)
    
i1 = 16
i2 = 5
i3 = 1 
solver = Solution()
print(solver.isPowerOfFour(i1))
print(solver.isPowerOfFour(i2))
print(solver.isPowerOfFour(i3))

