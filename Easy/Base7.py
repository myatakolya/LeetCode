'''
Problem: Base 7
Number: 99
Difficulty: Easy
Time Complexity: O(log₇(n))
Space Complexity: O(log₇(n))
URL: https://leetcode.com/problems/base-7
Topics: Math, String
'''
class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return '0'
        if num < 0:
            num = -num
            res = []
            while num > 0:
                res = [str(num % 7)] + res
                num = num//7
            return '-' + ''.join(res)
        else:
            res = []
            while num > 0:
                res = [str(num % 7)] + res
                num = num//7
            return ''.join(res)


s = Solution()
n1 = 100
n2 = -7
print(s.convertToBase7(n1))
print(s.convertToBase7(n2))