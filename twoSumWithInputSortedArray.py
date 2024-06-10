class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        size = len(numbers)

        if size < 2:
            return []

        left, right = 0, size-1

        while left < right:
            value = numbers[left] + numbers[right]

            if value == target:
                return [left+1, right+1]
            elif value < target:
                left += 1
            else:
                right -= 1

        return []
