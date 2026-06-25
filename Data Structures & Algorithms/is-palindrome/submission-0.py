class Solution:
    def isPalindrome(self, s: str) -> bool:
        # s = "QWE RTY?"

        clean = "".join(c.lower() for c in s if (c.isalnum()))

        if (clean == clean[::-1]):
            return True

        return False