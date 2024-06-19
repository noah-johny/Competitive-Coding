class Solution:
    def search(self, nums: List[int], target: int) -> int:
        beg, end = 0, len(nums)-1

        while beg <= end:
            mid = (beg+end) // 2

            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                end = mid-1
            else:
                beg = mid+1

        return -1