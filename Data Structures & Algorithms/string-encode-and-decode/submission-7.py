class Solution:

    def encode(self, strs: List[str]) -> str:
        
        encodedString = " ".join(string for string in strs)

        print(encodedString)

        return encodedString

    def decode(self, s: str) -> List[str]:
        return [] if s.split(" ") == " " else s.split(" ")
