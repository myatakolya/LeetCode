'''
Problem: Power of Two
Number: 5
Difficulty: Easy
Time Complexity: O(1)
Space Complexity: O(1)
URL: https://leetcode.com/problems/power-of-two
Topics: Math, Bit Manipulation
'''
class Solution:
    
    #Time Complexity: O(1)
    #Space Complexity: O(1)
    def isPowerOfTwo1(self, n: int) -> bool:
        return (n>0) and (n & (n-1) == 0)
    
    
    #Time Complexity: O(log n)
    #Space Complexity: O(log n)
    def isPowerOfTwo2(self, n: int) -> bool:
        
        def helper(n:int) -> bool:
            if n == 1:
                return True
            if n % 2 == 0:
                return helper(n//2)
            return False
        
        if n == 1:
            return True
        elif n % 2 != 0 or n <= 0:
            return False
        else:
            return helper(n)
        
    #Time Complexity: O(log n)
    #Space Complexity: O(log n)
    def isPowerOfTwo3(self, n: int) -> bool:
        if n == 1:
            return True
        elif n % 2 != 0:
            return False
        else:
            bin_n = f'{n:b}'
            if bin_n[0] == '1' and bin_n.count('1') == 1:
                return True
        return False
    
    
n1 = 1
n2 = 16
n3 = 3
solver = Solution()
print(solver.isPowerOfTwo(n1))
print(solver.isPowerOfTwo(n2))
print(solver.isPowerOfTwo(n3))