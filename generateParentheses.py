class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def generate(l, r, sen):
            if len(sen) == n * 2:
                res.append(sen)
                return
            
            if l < n:
                generate(l+1, r, sen+"(")

            if r < l:
                generate(l, r+1, sen+")")

        res = []
        generate(0, 0, "")
        return res