class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtracking(n, res, l, r, str):
            if l < r:
                return
            if l == r & r == n:
                res.append(str)
                return
            if l < n:
                backtracking(n, res, l + 1, r, str + "(")
            if l > r:
                backtracking(n, res, l, r + 1, str + ")")

        backtracking(n, res, 0, 0, "")
        return res