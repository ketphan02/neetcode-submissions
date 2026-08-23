class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            bit_at_i = ((1 << i) & n) >> i
            reverse_pos = 32 - i - 1
            res |= bit_at_i << reverse_pos
        return res