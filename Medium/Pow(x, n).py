'''
Problem: Pow(x, n)
Number: 4
Difficulty: Medium
Time Complexity: O(log n)
Space Complexity: O(log n)
URL: https://leetcode.com/problems/powx-n
Topics: Math, Recursion, Binary Exponentiation
'''
class Solution:
    def myPow(self, x: float, n: int) -> float:
        def pos_pow(x, n):
            if n == 0:
                return 1.0
            half = pos_pow(x,n//2)
            if n % 2 == 0:
                return half*half
            else:
                return x*half*half
        
        if n > 0:
            return pos_pow(x, n)  
        else:
            return 1 / pos_pow(x, -n)
            
    
x1 = 2.00000
n1 = 10
x2 = 2.10000
n2 = 3
x3 = 2.00000
n3 = -2
x4 = 2.00000
n4 = -3
solver = Solution()
print(solver.myPow(x1,n1))
print(solver.myPow(x2,n3))
print(solver.myPow(x3,n3))
print(solver.myPow(x4,n4))