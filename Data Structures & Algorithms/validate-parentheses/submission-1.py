from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        for c in s:
            try:
                if c == '}' and stack.pop() != '{':
                    return False
                elif c == ']' and stack.pop() != '[':
                    return False
                elif c == ')' and stack.pop() != '(':
                    return False
            except:
                return False
            if c in ['[', '{', '(']:
                stack.append(c)
        return len(stack) == 0

