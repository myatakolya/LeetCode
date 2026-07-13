import math
'''
Problem: Permutation Sequence
Number: 23
Difficulty: Medium
Time Complexity: O(n²)
Space Complexity: O(n)
URL: https://leetcode.com/problems/permutation-sequence
Topics: Math, Backtracking, Factorial Number System
'''

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        digits = [i for i in range(1,n+1)]
        fact = math.factorial(n-1)
        res = ''
        k = k-1
        for i in range(1,n+1):
            fact = math.factorial(n-i)
            index = k // fact
            res += str(digits[index])
            digits.remove(digits[index])
            k = k % fact
        return ''.join(res)
                        
    
n1 = 3
k1 = 3
n2 = 4
k2 = 9
n3 = 3
k3 = 1
s = Solution()
print(s.getPermutation(n1,k1))
print(s.getPermutation(n2,k2))
print(s.getPermutation(n3,k3))