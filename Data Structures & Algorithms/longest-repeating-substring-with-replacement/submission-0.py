class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        l = 0

        length = 0

        for r in range(len(s)):
            
            windowLength = r - l + 1

            letterCount = Counter(s[l:r + 1])

            mostCommon = letterCount.most_common()[0][1]

            if windowLength - mostCommon > k:
                l += 1
            
            length = max(length, r - l + 1)
            
        return length 


