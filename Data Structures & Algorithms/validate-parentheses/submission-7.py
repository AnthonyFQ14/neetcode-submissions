class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []

        for c in s:

            if c in ")":
                if stack and stack[-1] == "(":
                    stack.pop()
            elif c in "}":
                if stack and stack[-1] == "{":
                    stack.pop()
            elif c in "]":
                if stack and stack[-1] == "[":
                    stack.pop()
            else: 
                stack.append(c)
        print(stack)
        return not stack