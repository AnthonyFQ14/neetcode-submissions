class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        maxArea = 0

        for i, height in enumerate(heights):
            
            l = i
            r = len(heights) - 1

            while l < r:

                area = min(heights[l], heights[r]) * (r - l)

                maxArea = max(maxArea, area)

                l += 1
                r -= 1

        return maxArea

