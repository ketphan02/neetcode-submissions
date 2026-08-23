class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hsh = defaultdict(int)
        for num in nums:
            hsh[num] += 1
        s = sorted([(v, k) for k, v in hsh.items()], reverse=True)[:k]
        return list(map(lambda x: x[1], s))