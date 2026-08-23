class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hsh = defaultdict()

        for idx, num in enumerate(nums):
            need = target - num
            if need in hsh:
                return [hsh[need], idx]
            
            hsh[num] = idx
        return [-1, -1]