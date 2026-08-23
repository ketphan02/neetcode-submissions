from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_counter = Counter(t)
        def is_suffice(s_counter):
            for key in t_counter.keys():
                if key not in s_counter:
                    return False
                if s_counter[key] < t_counter[key]:
                    return False
            return True

        def check(start_position):
            cur_s = defaultdict(int)
            can_continue = False
            for end in range(start_position, len(s)):
                cur_s[s[end]] += 1
                if is_suffice(cur_s):
                    can_continue = True
                    break
            
            start = start_position
            res = ""
            while start <= end and is_suffice(cur_s):
                res = s[start:end+1]
                cur_s[s[start]] -= 1
                if cur_s[s[start]] == 0:
                    del cur_s[s[start]]
                start += 1

            return res

        res = ""
        for i in range(len(s) - len(t) + 1):
            local = check(i)
            if local == "":
                continue
            if res == "" or len(local) < len(res):
                res = local
        return res