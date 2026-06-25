
class Solution:
    def trap(self, height: List[int]) -> int:
        
        trapped = 0

        l = 0
        r = len(height) - 1

        leftMax = height[l]
        rightMax = height[r]

        while l < r:

            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                trapped += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                trapped += rightMax - height[r]
        
        return trapped


