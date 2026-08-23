class Solution:

    def search(self, nums: List[int], target: int) -> int:

        # return index of min
        def find_min_idx():
            low, high = 0, len(nums) - 1
            while low <= high:
                if nums[low] < nums[high]:
                    return low
                mid = (low + high) // 2
                if nums[mid] < nums[high]:
                    high = mid
                else:
                    low = mid + 1
            return high

        def find_num_idx(low, high):
            while low <= high:
                mid = (low + high) // 2
                if nums[mid] == target:
                    return mid
                if nums[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1
            return -1

        min_idx = find_min_idx()
        if nums[min_idx] == target:
            return min_idx
        l, r = find_num_idx(0, min_idx - 1), find_num_idx(min_idx, len(nums) - 1)
        print(min_idx, l, r)
        if l == -1 and r == -1:
            return -1
        if l == -1:
            return r
        return l