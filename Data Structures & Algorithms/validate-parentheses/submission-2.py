class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        key = {
            "]":"[",
            "}":"{",
            ")":"("
        }
        for p in s:
            if not p in key:
                stack.append(p)
                continue
            if len(stack) == 0:
                return False
            if stack[-1] != key[p]:
                return False
            stack.pop()
        return stack == []