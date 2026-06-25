class Solution:

    
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        output = []

        total = 1
        for i in range(len(nums)):
            output.append(total)    # total holds product of everything BEFORE i
            total *= nums[i]        # now include nums[i] for future iterations

        suffix = 1
        for i in reversed(range(len(nums))):
            output[i] *= suffix    # multiply by product of everything AFTER i
            suffix *= nums[i]      # include nums[i] for future iterations

        return output
    