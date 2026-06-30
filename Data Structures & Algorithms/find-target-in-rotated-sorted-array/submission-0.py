class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l = 0
        r = len(nums) - 1

        while l <= r:
            
            mid = (l + r) // 2

            if nums[l] < nums[r]:

                if nums[mid] < target and l <= r:
                    l = mid + 1
                elif nums[mid] > target and l <= r:
                    r = mid - 1
                else:
                    return mid
            

            if nums[mid] == target:
                return mid
            elif nums[mid] > nums[l] and nums[mid] > target:
                l = mid + 1
            elif nums[mid] < nums[l] and nums[mid] < target:
                r = mid - 1
        return -1