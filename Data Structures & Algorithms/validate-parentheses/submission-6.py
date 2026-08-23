class Solution:
    def isValid(self, s: str) -> bool:
        m = {
            "}": "{",
            "]": "[",
            ")": "("
        }

        stack = []
        for c in s:
            if c not in m:
                stack.append(c)
            else:
                need = m[c]
                if not stack or need != stack[-1]:
                    return False
                stack.pop()
        return not stack