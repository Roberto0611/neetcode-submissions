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
                # es de apertura
                stack.append(p)
                continue
            # es de cierre
            if len(stack) == 0:
                return False

            if stack[-1] != key[p]:
                return False
            stack.pop()
        if len(stack) == 0:
            return True
        return False