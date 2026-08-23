class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def evaluate(a, b, sign):
            if sign == '+':
                return a + b
            if sign == '-':
                return a - b
            if sign == '*':
                return a * b
            if sign == '/':
                return int(float(a) / b)
        
        stack = []
        for token in tokens:
            if token not in ["+", "-", "*", "/"]:
                stack.append(int(token))
                continue
            
            b = stack.pop()
            a = stack.pop()
            new_num = evaluate(a, b, token)
            stack.append(new_num)
        
        return round(stack[0])