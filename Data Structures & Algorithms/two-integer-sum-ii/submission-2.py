class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        

        indexes = {}
        for i in range(len(numbers)):
            indexes[i] = numbers[i]
        
        print("Indexes", indexes)

        compliments = {}

        for num in numbers:
            compliments[num] = target - num
        print("Compliments", compliments)

        for i, compliment in enumerate(compliments):
            comp_value = compliments[compliment]
            if comp_value in numbers:
                j = numbers.index(comp_value)
                if i != j:
                    return [i + 1, j + 1]
        return [0]