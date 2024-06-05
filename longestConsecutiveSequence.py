class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
            return 0

        nums = list(set(nums))
        nums.sort()
        start, length = nums[0], 1
        longest_length = set()

        for i in range(1, len(nums)):
            if nums[i] != start+1:
                longest_length.add(length)
                start = nums[i]
                length = 0
            else:
                start += 1

            length += 1

        longest_length.add(length)
        return max(longest_length)