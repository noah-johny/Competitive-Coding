class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total_product, total_non_zero_product = 1, 1
        zeroes, result = 0, []

        for num in nums:
            if num == 0:
                zeroes += 1
            else:
                total_non_zero_product *= num
        
        if zeroes > 0:
            if zeroes == 1:
                for num in nums:
                    if num != 0:
                        result.append(0)
                    else:
                        result.append(total_non_zero_product)
            else:
                for i in nums:
                    result.append(0)
        else:
            for num in nums:
                result.append(total_non_zero_product // num)

        return result