from collections import deque
'''
Problem: Rotate String
Number: 78
Difficulty: Easy
Time Complexity: O(n)
Space Complexity: O(n)
URL: https://leetcode.com/problems/rotate-string
Topics: String, String Matching
'''
class Solution:
    
    #Time Complexity: O(n²)
    #Space Complexity: O(n)
    def rotateString_1(self, s: str, goal: str) -> bool:
        eque = deque(s)
        n = len(s)
        while n:
            eque.append(eque.popleft())
            if ''.join(eque) == goal:
                return True
            n -= 1
        return False
    
    def rotateString(self, s: str, goal: str) -> bool:
        return len(s) == len(goal) and goal in s + s

s = 'abcde'
g = 'cdeab'
solver = Solution()
print(solver.rotateString(s,g))