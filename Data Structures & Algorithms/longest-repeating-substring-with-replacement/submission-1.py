class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        l = 0

        length = 0

        letterCount = {}

        for r in range(len(s)):
            
            letterCount[s[r]] = 1 + letterCount.get(s[r], 0)

            mostCommon = max(letterCount.values())

            if (r - l + 1) - mostCommon > k:
                l += 1
                letterCount[s[l]] -= 1
            
            length = max(length, r - l + 1)
            
        return length 


