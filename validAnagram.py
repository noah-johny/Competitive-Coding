class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        else:
            for letter in s:
                if letter not in t:
                    return False
                else:
                    t = t.replace(letter, "", 1)

            return True