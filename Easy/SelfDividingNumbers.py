from typing import List
'''
Problem: Self Dividing Numbers
Number: 57
Difficulty: Easy
Time Complexity: O(n*d)
Space Complexity: O(1)
URL: https://leetcode.com/problems/self-dividing-numbers
Topics: Math, Number Theory
'''
class Solution:
    def is_self_dividing(self,n):
        if n % 10 == 0:
            return False
        elif 1<=n<=9:
            return True
        else:
            temp = n
            while temp > 0:
                digit = temp%10
                if digit == 0:
                    return False
                elif n % digit != 0:
                    return False
                temp = temp//10
            return True
                
    
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        return [i for i in range(left,right+1) if self.is_self_dividing(i)==True]
    
s = Solution()
l1,r1 = 1,22
l2,r2 = 47,85
print(s.selfDividingNumbers(l1,r1))
print(s.selfDividingNumbers(l2,r2))