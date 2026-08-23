import uuid

class Solution:
    PATTERN = "ååß∂åßåß∂∂åßåß∂"
    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        return self.PATTERN.join(strs) + self.PATTERN

    def decode(self, s: str) -> List[str]:
        if s == "":
            return []
        return s.rstrip(self.PATTERN).split(self.PATTERN)
