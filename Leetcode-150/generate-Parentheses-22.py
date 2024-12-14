"""
    Given n pairs of parentheses, write a function to generate
    all combinations of well-formed parentheses.

    ex : Input: n = 3
    Output: ["((()))","(()())","(())()","()(())","()()()"]
"""
# Draw a decision Tree to understand this we have two choices we can have an open '('
# we can also include ')' when if and only closeP is < openP because that would cause
# an invalid solution if we include ')'

from typing import List
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def dfs(openP, closeP, s: str):
            if openP == closeP == n:
                res.append(s)
                return
            if openP < n:
                dfs(openP+1 , closeP, s+'(')
            if closeP < openP:
                dfs(openP, closeP+1, s+')')
        dfs(0, 0, "")
        return res