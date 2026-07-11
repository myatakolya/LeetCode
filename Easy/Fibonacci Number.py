from functools import cache
class Solution: 
    #Time Complexity: O(n)
    #Space Complexity: O(1)
    def fib1(self, n: int) -> int:
        if n <= 1:
            return n
        else:
            summa = 0
            prev1,prev2 = 1, 0
            for _ in range(2,n+1):
                summa = prev1 + prev2
                prev1,prev2 = summa, prev1
                
            return summa
        
    #Time Complexity: O(n)
    #Space Complexity: O(n)
    def fib(self, n: int) -> int:
        @cache
        def f(n):
            if n <= 1:
                return n
            else:
                return f(n-1) + f(n-2)
        return f(n)

i1 = 2
i2 = 3
i3 = 4
solver = Solution()
print(solver.fib(i1))
print(solver.fib(i2))
print(solver.fib(i3))