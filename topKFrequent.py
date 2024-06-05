from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_frequency = Counter(nums)
        result = []

        sorted_tuple_list = sorted(tuple(nums_frequency.items()), key=lambda x:x[1], reverse=True)

        for i in range(k):
            result.append(sorted_tuple_list[i][0])

        return result
