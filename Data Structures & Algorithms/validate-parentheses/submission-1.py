class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for c in s:

            # if stack is empty and first character is a closing not valid
            if not stack and c in {')', '}', ']'} :
                return False
            # stack has something in it and current character is ) check if top of stack is (
            elif stack and c == ')':
                if stack[-1] == '(':
                    stack.pop()
            
            elif stack and c == '}':
                if stack[-1] == '{':
                    stack.pop()
                
            elif stack and c == ']':
                if stack[-1] == '[':
                    stack.pop()
            else:
                stack.append(c)
    
        return not stack