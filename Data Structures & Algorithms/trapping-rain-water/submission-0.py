# anything to the left of the first bar and last bar ignore
# 

class Solution:
    def trap(self, height: List[int]) -> int:
        
        trapped = 0

        leftMax = [0] * len(height)
        rightMax = [0] * len(height)

        l_max = 0
        for i in range(len(height)):
            leftMax[i] = l_max  # Store max of everything BEFORE index i
            l_max = max(l_max, height[i]) # Update for the next index

        r_max = 0
        for i in range(len(height) - 1, -1, -1):
            rightMax[i] = r_max  # Store max of everything BEFORE index i
            r_max = max(r_max, height[i]) # Update for the next index

        for i in range(len(height)):
            tmp = (min(leftMax[i], rightMax[i]) - height[i])
            if tmp >= 0:
                trapped += tmp

        print(leftMax)
        print(rightMax)
        return trapped
