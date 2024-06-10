class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        size = len(nums)

        if size < 3:
            return []
        elif size == 3:
            if sum(nums) == 0:
                return [nums]
            else:
                return []
        
        nums.sort()
        result = []

        for i in range(size):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            j, k = i+1, size-1

            while j < k:
                value = nums[i] + nums[j] + nums[k]

                if value == 0:
                    result.append([nums[i], nums[j], nums[k]])
                    j += 1

                    while nums[j] == nums[j-1] and j < k:
                        j += 1

                elif value < 0:
                    j += 1
                else:
                    k -= 1

        return result