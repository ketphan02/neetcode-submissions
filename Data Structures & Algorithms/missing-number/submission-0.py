class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        total_xor = 0
        for i in range(len(nums) + 1):
            total_xor ^= i
        
        for num in nums:
            total_xor ^= num
        return total_xor