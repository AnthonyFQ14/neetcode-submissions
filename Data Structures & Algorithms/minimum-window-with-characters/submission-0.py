class Solution:
    def minWindow(self, s: str, t: str) -> str:

        charsT = Counter(t)
        charsS = Counter()
        l = 0
        minLength = 1001
        windows = {}
        for r in range(len(s)):
            charsS[(s[r])] += 1

            if (r - l + 1) >= len(t):
                while charsT <= charsS:
                    minLength = min(minLength, r - l + 1)
                    windows[minLength] = [r, l]
                charsS[s[l]] -= 1
                l += 1
        if not windows:
            return ""
        minWindow = min(windows)
        
        rightIndex = windows[minWindow][0]
        leftIndex = windows[minWindow][1]

        return s[leftIndex: rightIndex + 1]