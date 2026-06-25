class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for c in s:

            if not stack and c in {')', '}', ']'} :
                return False
            elif stack and c == ')':
                if stack[-1] == '(':
                    stack.pop()
                else:
                    return False
            elif stack and c == '}':
                if stack[-1] == '{':
                    stack.pop()
                else:
                    return False
            elif stack and c == ']':
                if stack[-1] == '[':
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        return not stack
