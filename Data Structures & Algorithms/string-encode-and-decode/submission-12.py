class Solution:

    name = "World"
    result = f"Hello {name}!"  # Result: "Hello World!"

    def encode(self, strs: List[str]) -> str:
        
        # encodedString = " ".join(string for string in strs)
        encodedString = ""
        encodedString += str(len(strs))
        for word in strs:
            length = len(word)
            encodedString += str(length) + word

        print("Encoded String: ", encodedString)

        return encodedString

    def decode(self, s: str) -> List[str]:
        print(s)
        # print(s[8])
        # end index should be 12
        8 + 5 - 1 

        decodedMessage = []

        d = {}
        wordStartIndex = 2
        wordEndIndex = int(s[1]) + 2

        for i in range(int(s[0])):
            print("Start index", wordStartIndex)
            print("End index", wordEndIndex)
            d[i] = s[wordStartIndex : wordEndIndex]
            wordStartIndex = wordEndIndex + 1

            nextWordLength = wordEndIndex

            print("NEXT WORD LENGTH" , nextWordLength)

            wordEndIndex = wordStartIndex + nextWordLength - 1

        # print("int(s[wordStartIndex]", int(s[wordStartIndex - 1]))
        
        print(d)
        return list(d.values())





