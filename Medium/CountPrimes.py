'''
Problem: Count Primes
Number: 62
Difficulty: Easy
Time Complexity: O(n*log(log(n)))
Space Complexity: O(n)
URL: https://leetcode.com/problems/count-primes
Topics: Math, Array, Sieve
'''
class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 3:
            return 0
        else:
            is_prime = [True] * n
            is_prime[0],is_prime[1] = False,False
            for i in range(2,int(n**0.5)+1):
                if is_prime[i] == True:
                    for j in range(i*i,n,i):
                        is_prime[j] = False
            res = 0
            for i in is_prime:
                if i == True:
                    res += 1
            return res