class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        slow = 0
        fast = 1

        while slow < len(nums) - 1:
            if nums[slow] == nums[fast]:
                return nums[slow]
            slow += 1
            if fast + 2 < len(nums) - 1:
                fast += 2
        
