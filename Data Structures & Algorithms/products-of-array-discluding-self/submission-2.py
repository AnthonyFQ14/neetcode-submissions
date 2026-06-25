class Solution:
    
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []

        prefix = 1
        for i in range(len(nums)):
            output.append(prefix)
            prefix *= nums[i]

        suffix = 1
        for i in reversed(range(len(nums))):
            output[i] *= suffix
            suffix *= nums[i]

        return output