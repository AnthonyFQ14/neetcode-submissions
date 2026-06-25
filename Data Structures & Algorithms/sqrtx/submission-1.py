class Solution:
    def mySqrt(self, x: int) -> int:
        
        largest = 0
        left = 0
        right = x

        while left <= right:
            mid = (left + right) // 2

            if mid * mid == x:
                return mid
            elif mid * mid < x:
                largest = mid
                left = mid + 1
            elif mid * mid > x:
                right = mid - 1
        return largest
