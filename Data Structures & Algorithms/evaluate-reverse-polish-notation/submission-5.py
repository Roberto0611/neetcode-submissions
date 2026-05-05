class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operations = {"+","-","*","/"}
        
        for char in tokens:
            if not char in operations:
                # es numero
                stack.append(int(char))
                continue
            # es simbolo
            match char:
                case "+":
                    output = stack.pop() + stack.pop()
                    stack.append(output)
                    print(output)
                case "-":
                    output = stack.pop(-2) - stack.pop()
                    stack.append(output)
                    print(output)
                case "/":
                    output = int(stack.pop(-2) / stack.pop())
                    stack.append(output)
                    print(output)
                case "*":
                    output = stack.pop() * stack.pop()
                    stack.append(output)
                    print(output)
        return stack[-1]