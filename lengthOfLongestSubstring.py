class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        size = len(s)
        substring, substringLength = "", 0
        i = 0

        while i < size:
            if s[i] not in substring:
                substring += s[i]
            else:
                if len(substring) > substringLength:
                    substringLength = len(substring)

                substring = "" if len(substring) <= 1 else substring[1:]
                i -= 1

            i += 1

        if len(substring) > substringLength:
            substringLength = len(substring)

        return substringLength