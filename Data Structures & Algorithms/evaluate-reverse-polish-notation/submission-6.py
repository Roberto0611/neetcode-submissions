class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operations = {"+","-","*","/"}
        
        for char in tokens:
            if not char in operations:
                stack.append(int(char))
                continue
            match char:
                case "+":
                    stack.append(stack.pop() + stack.pop())
                case "-":
                    a,b = stack.pop(),stack.pop()
                    stack.append(b - a)
                case "/":
                    a,b = stack.pop(),stack.pop()
                    stack.append(int(b / a))
                case "*":
                    stack.append(stack.pop() * stack.pop())
        return stack.pop()