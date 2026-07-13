from typing import List

'''
Problem: Partition Array into Two Equal Product Subsets
Number: 20
Difficulty: Medium
Time Complexity: O((2^n)*n)
Space Complexity: O(1)
URL: https://leetcode.com/problems/partition-array-into-two-equal-product-subsets
Topics: Array, Bit Manipulation, Enumeration
'''

class Solution:
    def checkEqualPartitions(self, nums: List[int], target: int) -> bool:
        n = len(nums)
        for mask in range(1<<n):
            if mask != 0 and mask != (1<<n)-1:
                first_prod = 1
                second_prod = 1
                for j,num in enumerate(nums):
                    if (mask >> j) & 1:
                        first_prod *= num
                    else:
                        second_prod *= num
                if first_prod == target and second_prod == target:
                    return True
        return False
                

i1,t1 = [3,1,6,8,4,],24
i2,t2 = [2,5,3,7],15
s = Solution()
print(s.checkEqualPartitions(i1,t1))
print(s.checkEqualPartitions(i2,t2))