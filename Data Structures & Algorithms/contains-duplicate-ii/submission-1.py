class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        lastIdx = {}
        for idx, num in enumerate(nums):
            if num in lastIdx and idx - lastIdx[num] <= k:
                return True
            lastIdx[num] = idx

        return False
