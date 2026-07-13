'''
Problem: Elimination Game
Number: 12
Difficulty: Medium
Time Complexity: O(log n)
Space Complexity: O(1)
URL: https://leetcode.com/problems/elimination-game
Topics: Math, Recursion, Simulation
'''
class Solution:        
    def lastRemaining(self, n: int) -> int:
        first, last = 1,n
        remainig = n
        step = 1
        l_to_r = True
        while remainig > 1:
            if l_to_r == True:
                if remainig % 2 != 0:
                    last = last - step
                first = first + step
            if l_to_r == False:
                if remainig % 2 != 0:
                    first = first + step
                last = last - step
            remainig = remainig // 2
            step = step * 2
            l_to_r = not l_to_r
        return first
        
        
solver = Solution()
i1 = 9
i2 = 1
print(solver.lastRemaining(i1))
print(solver.lastRemaining(i2))