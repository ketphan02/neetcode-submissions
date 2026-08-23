class Solution:

    DELIMETER = "!"

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for s in strs:
            encoded_str += f"{len(s)}{self.DELIMETER}{s}"
        
        return encoded_str


    def decode(self, s: str) -> List[str]:
        res = []
        num = 0
        while s:
            if s[0] == self.DELIMETER:
                res.append(s[1:num + 1])
                s = s[num + 1:]
                num = 0
            else:
                num = num * 10 + int(s[0])
                s = s[1:]
        return res