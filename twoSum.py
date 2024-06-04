class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {}
        result = []

        for i, num in enumerate(nums):
            if num not in nums_dict:
                nums_dict[num] = [i]
            else:
                nums_dict[num].append(i)

        for i, num in enumerate(nums):
            diff = target - num
            if diff in nums_dict:
                index = nums_dict[diff][0]

                if index == i:
                    if len(nums_dict[diff]) == 1:
                        continue
                    else:
                        index = nums_dict[diff][1]

                return [i, index]

        return []