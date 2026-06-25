class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        nums = sorted(nums1 + nums2)
        median = 0
        print(nums)
        if len(nums) % 2 == 0:
            median = (nums[(len(nums) - 1) // 2] + nums[((len(nums) - 1) // 2) + 1]) / 2
        else:
            median = nums[len(nums) // 2]
        return median