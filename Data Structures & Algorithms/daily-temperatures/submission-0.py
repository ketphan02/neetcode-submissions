class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0 for _ in temperatures]
        stack = []
        for idx, temp in enumerate(temperatures):
            while len(stack) > 0 and stack[-1][0] < temp:
                done = stack.pop()
                res[done[1]] = idx - done[1]

            stack.append((temp, idx))
                
        return res