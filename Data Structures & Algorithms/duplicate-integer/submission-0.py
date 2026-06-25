class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        d = {}

        for i, num in enumerate(nums):
            if ( d.get(num, -1) != -1 ):
                return True
            else:
                d[num] = i
        return False