'''
Problem: Power of Three
Number: 6
Difficulty: Easy
Time Complexity: O(1)
Space Complexity: O(1)
URL: https://leetcode.com/problems/power-of-three
Topics: Math, Recursion (но решено без рекурсии)
'''
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        return (n>0) and (3**19 % n == 0)
    
i1 = 27
i2 = 0
i3 = -1
solver = Solution()
print(solver.isPowerOfThree(i1))
print(solver.isPowerOfThree(i2))
print(solver.isPowerOfThree(i3))