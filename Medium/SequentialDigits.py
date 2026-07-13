from typing import List

'''
Problem: Sequential Digits
Number: 19
Difficulty: Medium
Time Complexity: O(1)
Space Complexity: O(1)
URL: https://leetcode.com/problems/sequential-digits
Topics: Enumeration, Backtracking, Math
'''

class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        result_list = []
        digits = '123456789'
        n = len(str(low))
        while n < len(digits):
            start = 0
            while start <= len(digits)-n:
                result_list.append(int(digits[start:start+n]))
                start += 1
            n += 1
        result_list.append(int('123456789'))
        return [i for i in result_list if low<=i<=high]
           
            
                
l1,h1 = 100,300
l2,h2 = 1000,13000
s = Solution()
print(s.sequentialDigits(l1,h1))
print(s.sequentialDigits(l2,h2))