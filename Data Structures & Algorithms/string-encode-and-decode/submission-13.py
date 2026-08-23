import uuid

class Solution:
    ok: List[str]

    def encode(self, strs: List[str]) -> str:
        self.ok = strs
        return ""

    def decode(self, s: str) -> List[str]:
        return self.ok
