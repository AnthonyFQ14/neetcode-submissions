class Solution:
    def isPalindrome(self, s: str) -> bool:

        cleanString = "".join(c.lower() for c in s if c.isalnum())
        
        return cleanString == cleanString[::-1]



