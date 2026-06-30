class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        

        indexes = {}
        for i in range(len(numbers)):
            indexes[i] = numbers[i]
        
        print(indexes)

        compliments = {}

        for num in numbers:
            compliments[num] = target - num
        print(compliments)

        for num, compliment in enumerate(compliments):
            print(compliment, compliments[compliment])
            if compliment in numbers and compliments[compliment] in numbers:
                return [indexes.get(compliment) - 1, indexes.get(compliments[compliment]) - 1]
        return [0]