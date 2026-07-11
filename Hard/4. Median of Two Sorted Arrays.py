class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums3 = sorted(nums1 + nums2)
        half = len(nums3)//2
        if len(nums3) % 2 != 0:
            return nums3[half]
        else:
            return (nums3[half] + nums3[half-1])/2
