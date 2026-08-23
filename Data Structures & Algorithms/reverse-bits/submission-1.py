class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        num_need_shift = 32
        for i in range(16):
            bit_at_i = ((1 << i) & n)
            res |= bit_at_i << num_need_shift - 1
            num_need_shift -= 2
        num_need_shift = 1
        for i in range(16, 32):
            bit_at_i = ((1 << i) & n)
            res |= bit_at_i >> num_need_shift
            num_need_shift += 2
        return res