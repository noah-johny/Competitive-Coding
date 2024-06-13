from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Size, s2Size = len(s1), len(s2)
        s1FrequencyDict = Counter(list(s1))
        s2FrequencyDict = Counter(list(s2[:s1Size]))
        l, r = 0, s1Size-1

        while r < s2Size:
            if s1FrequencyDict == s2FrequencyDict:
                return True
            else:
                r += 1

                if r < s2Size:
                    s2FrequencyDict[s2[r]] = s2FrequencyDict.get(s2[r], 0) + 1
                else:
                    break

                if s2[l] in s2FrequencyDict:
                    if s2FrequencyDict[s2[l]] == 1:
                        s2FrequencyDict.pop(s2[l])
                    else:
                        s2FrequencyDict[s2[l]] -= 1
                
                l += 1

        return False