class Solution:
    def findMin(self, nums: List[int]) -> int:
        size = len(nums)
        beg, end = 0, size-1
        minVal = nums[0]

        while beg < end:
            mid = (beg+end) // 2
            if nums[mid] >= nums[beg]:
                beg = mid+1
                minVal = min(minVal, nums[beg])
            elif nums[mid] < nums[beg]:
                end = mid-1
                minVal = min(minVal, nums[mid])

        return minVal