class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        res = 0
        numbers = []
        operands = []


        # 1 2 3 4
        # + * -

        for t in tokens:
            if t.isnumeric():
                numbers.append(t)
            elif t in {"+", "-", "*", "/"}:
                operands.append(t)
        
        print(numbers)
        print(operands)

        numbers.reverse()
        operands.reverse()

        print(numbers)
        print(operands)

        while numbers:

            exp = ""

            num1 = numbers.pop()
            num2 = ""
            
            if len(numbers) > 1:
                num2 = numbers.pop()

            operand = operands.pop()
            
            if num2 != "":
                exp += num1 + operand + num2
            else:
                exp += str(res) + operand + num1
        
            res = eval(exp)

            # evaluate the first 2 numbers expression
            # evalute the last expression result with next operand



        return res