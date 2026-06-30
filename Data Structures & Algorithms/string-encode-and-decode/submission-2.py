class Solution:

    def encode(self, strs: List[str]) -> str:
        print(" ".join(string for string in strs))
        encodedString = " ".join(string for string in strs)

        return "" if encodedString == " " else encodedString

    def decode(self, s: str) -> List[str]:
        return s.split(" ")
