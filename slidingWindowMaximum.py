from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        size = len(nums)

        if size == 0 or k == 0:
            return []
        if k == 1:
            return nums

        q = deque()
        l = r = 0
        result = []

        while r < size:
            while q and nums[r] > nums[q[-1]]:
                q.pop()

            q.append(r)

            if l > q[0]:
                q.popleft()

            if r+1 >= k:
                result.append(nums[q[0]])
                l += 1

            r += 1
            
        return result