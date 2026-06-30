class Solution:

    name = "World"
    result = f"Hello {name}!"  # Result: "Hello World!"

    def encode(self, strs: List[str]) -> str:
        
        # encodedString = " ".join(string for string in strs)
        encodedString = ""
        encodedString += str(len(strs))
        for word in strs:
            length = len(word)
            # if length == 0:
            #     encodedString += str(1) + " " 
            encodedString += str(length) + word

        print("Encoded String: ", encodedString)

        return encodedString

    def decode(self, s: str) -> List[str]:
        print("String" , s)
        # print(s[8])
        # end index should be 12
        8 + 5 - 1 

        decodedMessage = []

        d = {}
        wordStartIndex = 2
        # if len(s)
        if s == "0":
            return []
        wordEndIndex = int(s[1]) + 2
        nextWordLength = 0

        for i in range(int(s[0])):
            print("Start index", wordStartIndex)
            print("End index", wordEndIndex)

            
            d[i] = s[wordStartIndex : wordEndIndex]
            print("Word: ", i, d[i])


            wordStartIndex = wordEndIndex + 1

            if wordEndIndex < len(s):
                nextWordLength = int(s[wordEndIndex])

            print("NEXT WORD LENGTH" , nextWordLength)

            wordEndIndex = wordStartIndex + nextWordLength # + 1

        # print("int(s[wordStartIndex]", int(s[wordStartIndex - 1]))
        
        print(d)
        # d.values()
        return list( val for val in d.values() if val != " ")





