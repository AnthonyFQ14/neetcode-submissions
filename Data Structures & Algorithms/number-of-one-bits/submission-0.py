class Solution:
    def hammingWeight(self, n: int) -> int:
        
        binary = bin(n)[2:]

        print(binary)

        string = [0] * 32

        

        # string[]

        counter = Counter(str(binary))

        print(counter['1'])
        return counter['1']