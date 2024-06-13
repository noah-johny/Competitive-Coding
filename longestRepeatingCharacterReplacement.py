class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        frequency = {}
        result = 0
        l = 0

        for r in range(len(s)):
            frequency[s[r]] = frequency.get(s[r], 0) + 1

            while (r-l+1) - max(frequency.values()) > k:
                frequency[s[l]] -= 1
                l += 1

            result = max(result, r-l+1)

        return result