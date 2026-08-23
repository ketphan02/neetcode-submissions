class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hsh = {}
        freq = [set() for _ in range(len(nums) + 1)]
        for num in nums:
            if num not in hsh:
                hsh[num] = 1
                freq[1].add(num)
            else:
                freq[hsh[num]].remove(num)
                hsh[num] += 1
                freq[hsh[num]].add(num)
        
        res = []
        for i in range(len(freq) - 1, -1, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) >= k:
                    return res
        return res