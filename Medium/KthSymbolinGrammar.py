'''
Problem: K-th Symbol in Grammar
Number: 14
Difficulty: Medium
Time Complexity: O(1)
Space Complexity: O(1)
URL: https://leetcode.com/problems/k-th-symbol-in-grammar
Topics: Math, Bit Manipulation, Recursion
'''

class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        return (k-1).bit_count() % 2
        
    
n1 = 1
k1 = 1
n2 = 2
k2 = 1
n3 = 2
k3 = 2
s = Solution()
print(s.kthGrammar(n1,k1))
print(s.kthGrammar(n2,k2))
print(s.kthGrammar(n3,k3))