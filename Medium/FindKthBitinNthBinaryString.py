'''
Problem: Find Kth Bit in Nth Binary String
Number: 15
Difficulty: Medium
Time Complexity: O(n)
Space Complexity: O(1)
URL: https://leetcode.com/problems/find-kth-bit-in-nth-binary-string
Topics: String, Recursion, Math, Bit Manipulation
'''
class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        inversion = False
        for i in range(n,1,-1):
            mid = 2**(i-1)
            if k == mid:
                if inversion == False:
                    return '1'
                else:
                    return '0'
            elif k > mid:
                k = 2*mid-k
                inversion = not inversion
        if inversion == False:
            return '0'
        else:
            return '1'
            
    
n1,k1 = 3,1
n2,k2 = 4,11
n3,k3 = 3,6
s = Solution()
print(s.findKthBit(n1,k1))
print(s.findKthBit(n3,k3))