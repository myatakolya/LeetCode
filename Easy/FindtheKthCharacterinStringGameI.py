
'''
Problem: Find the K-th Character in String Game I
Number: 10
Difficulty: Easy
Time Complexity: O(log k)
Space Complexity: O(1)
URL: https://leetcode.com/problems/find-the-k-th-character-in-string-game-i
Topics: Math, String, Recursion, Simulation
'''

class Solution:
    def kthCharacter(self, k: int) -> str:
        if k == 1: return 'a'
        n = 0
        while 2**n < k:
            n+=1
        offset = 0
        pos = k-1
        while n > 0:
            half = 2**(n-1)
            if pos < half:
                pass
            else:
                pos -= half
                offset += 1
            n -= 1
        return chr(ord('a') + offset)
        
            
    
i1 = 5
i2 = 10
solver = Solution()
print(solver.kthCharacter(i1))
print(solver.kthCharacter(i2))