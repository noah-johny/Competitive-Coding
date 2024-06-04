class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        distinct_nums = set(nums)

        if len(nums) == len(distinct_nums):
            return False
        else:
            return True