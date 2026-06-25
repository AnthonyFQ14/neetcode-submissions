class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        for i in range(len(numbers)):
            l = 0
            r = len(numbers) - 1
            complement = target - numbers[i]
            
            while l <= r:
                mid = (l + r) // 2
            
                if complement == numbers[mid]:
                    return [i + 1, mid + 1]
                elif numbers[mid] < complement:
                    l = mid + 1
                elif numbers[mid] > complement:
                    r = mid - 1
                

        return []