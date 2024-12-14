"""
    Given n pairs of parentheses, write a function to generate
    all combinations of well-formed parentheses.

    ex : Input: n = 3
    Output: ["((()))","(()())","(())()","()(())","()()()"]
"""
from typing import List
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        return