class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)

        print(count)
        print(count.most_common())
        
        output = []

        for i in range(k):
            output.append(count.most_common()[i][0])

        print(output)

        return output


