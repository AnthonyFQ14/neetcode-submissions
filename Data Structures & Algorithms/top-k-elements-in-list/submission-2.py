class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        
        # output = []

        # for i in range(k):
        #     output.append(count.most_common()[i][0])

        return [num for num, freq in count.most_common(k)]
        # return output
