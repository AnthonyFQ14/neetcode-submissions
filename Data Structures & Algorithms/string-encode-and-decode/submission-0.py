class Solution:

    def encode(self, strs: List[str]) -> str:
        print(" ".join(string for string in strs))
        return " ".join(string for string in strs)

    def decode(self, s: str) -> List[str]:
        return s.split(" ")
