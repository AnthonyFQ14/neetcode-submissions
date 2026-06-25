class Solution:

    def encode(self, strs: List[str]) -> str:
        
        encodedString = ""
        for word in strs:
            length = len(word)
            encodedString += str(length) + "#" + word
            print(length, word)

        print("Encoded String: ", encodedString)

        return encodedString

    def decode(self, s: str) -> List[str]:
        
        output = []
        print(s)

        i = 0
        while i < len(s):
            lengthStr = ""
            while s[i] != "#":
                lengthStr += s[i]
                i += 1

            i += 1

            output.append(s[i:i + int(lengthStr)])

            i = i + int(lengthStr)
            
        return output





