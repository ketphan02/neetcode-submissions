class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        current = defaultdict(int)
        h = []
        for idx in range(k):
            current[nums[idx]] += 1
            heapq.heappush(h, -nums[idx])
        
        res = []
        for end in range(k - 1, len(nums)):
            num = nums[end]
            start = end - k + 1
            
            if start > 0:
                current[num] += 1
                heapq.heappush(h, -num)
                current[nums[start - 1]] -= 1
                if current[nums[start - 1]] == 0:
                    del current[nums[start - 1]]
                while -h[0] not in current:
                    heapq.heappop(h)
            res.append(-h[0])
        
        return res
            