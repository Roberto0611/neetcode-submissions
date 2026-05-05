class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operations = {"+","-","*","/"}
        
        for char in tokens:
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
                case _:
                    stack.append(int(char))

        return stack.pop()