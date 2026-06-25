class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        compliments = {}

        for i in range(len(numbers)):
            compliment = target - numbers[i]
            if compliment in compliments:
                return [numbers.index(compliment) + 1, numbers.index(numbers[i]) + 1]
            compliments[numbers[i]] = compliment
        return []