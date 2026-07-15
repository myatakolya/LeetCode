from typing import List
'''
Problem: Closest Prime Numbers in Range
Number: 64
Difficulty: Medium
Time Complexity: O(n*log(log(n)))
Space Complexity: O(n)
URL: https://leetcode.com/problems/closest-prime-numbers-in-range
Topics: Math, Sieve
'''
class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        if right < 2:
            return [-1,-1]
        eratospher = [True] * (right+1)
        eratospher[0],eratospher[1] = False,False
        for i in range(2,len(eratospher)):
            for j in range(i*i,len(eratospher),i):
                eratospher[j] = False
        
        primes = [i for i in range(len(eratospher)) if i >= left and eratospher[i] == True]
        if len(primes) < 2:
            return [-1,-1]
        
        res = [primes[0],primes[1]]
        prev_abs = abs(primes[0] - primes[1])
        for i in range(len(primes)-1):
            cur_abs = abs(primes[i] - primes[i+1])
            if cur_abs < prev_abs:
                prev_abs = cur_abs
                res = [primes[i], primes[i+1]]
        return res
            
        
    
l1,r1 = 10,20
s = Solution()
print(s.closestPrimes(l1,r1))
        