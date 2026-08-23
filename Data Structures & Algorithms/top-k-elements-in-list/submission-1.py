class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        freq = [[] for _ in range(len(nums) + 1)]
        for key, v in count.items():
            freq[v].append(key)
        
        print(freq)
        res = []
        for idx in range(len(freq) - 1, 0, -1):
            for num in freq[idx]:
                res.append(num)
                if len(res) == k:
                    return res