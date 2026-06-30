class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        l = 0
        m = {}
        maxInWindow = float("-infinity")
        res = []
        for r in range(len(nums)):
            
            
            

            if (r - l + 1) > k:

                del m[l]
                l += 1

            m[r] = nums[r]
            maxInWindow = max(maxInWindow, nums[r])
            if (r - l + 1) == k:
                res.append(maxInWindow)

            print(nums[l: r + 1], maxInWindow)

        return res