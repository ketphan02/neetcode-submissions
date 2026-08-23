class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        keys = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }

        res = []
        
        def backtrack(digits, cur_s):
            nonlocal res
            if len(digits) <= 0:
                res.append(cur_s)
                return
            
            cur_digit = digits[0]
            digits = digits[1:]

            for v in keys[cur_digit]:
                backtrack(digits, cur_s + v)
        
        backtrack(digits, "")
        return res