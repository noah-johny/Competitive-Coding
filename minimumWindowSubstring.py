from collections import Counter

class Solution:
    def dictContains(self, dict1, dict2):
        for key, value in dict1.items():
            if key not in dict2 or dict2[key] < value:
                return False
        return True
    
    def minWindow(self, s: str, t: str) -> str:
        sLength, tLength = len(s), len(t)

        if sLength < tLength:
            return ""
        elif t in s:
            return t
        
        tDict = Counter(list(t))
        sDict = Counter(list(s[:tLength]))
        l, r = 0, tLength-1
        minSubstring = s
        check = False

        while r < sLength and l < r:
            if self.dictContains(tDict, sDict):
                if r-l+1 <= len(minSubstring):
                    minSubstring = s[l:(r+1)]
                    check = True

                if l < r:
                    if s[l] in sDict:
                        if sDict[s[l]] == 1:
                            sDict.pop(s[l])
                        else:
                            sDict[s[l]] -= 1

                    l += 1
            else:
                r += 1
                
                if r >= sLength:
                    break
                
                sDict[s[r]] = sDict.get(s[r], 0) + 1

        return minSubstring if check else ""
