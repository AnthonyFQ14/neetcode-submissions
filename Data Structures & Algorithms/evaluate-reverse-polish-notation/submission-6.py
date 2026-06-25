class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []

        for t in tokens:
            operator = ""
            exp = ""

            stack.append(t)
            
            if t in {"+", "-", "*", "/"}:
                operator += stack.pop()

                num1 = stack.pop()
                num2 = stack.pop()

                if operator == "/":
                    exp += "int(" + str(num2) + str(operator) + str(num1) + ")"
                else:
                    exp += str(num2) + str(operator) + str(num1)

                stack.append(eval(exp))
            
        return int(stack[0])