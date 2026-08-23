class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        pairs = sorted([(p, s) for p, s in zip(position, speed)], reverse=True)
        for p, s in pairs:
            cur_time_to_target = (target - p) / s
            if len(stack) == 0:
                stack.append(cur_time_to_target)
            elif stack[-1] < cur_time_to_target:
                stack.append(cur_time_to_target)

        return len(stack)