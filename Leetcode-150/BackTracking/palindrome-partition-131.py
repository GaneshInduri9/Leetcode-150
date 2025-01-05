"""
    Given a string s, partition s such that every substring of the partition is a 
    palindrome. Return all possible palindrome partitioning of s.
    Input: s = "aab"
    Output: [["a","a","b"],["aa","b"]]
"""
from typing import List
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        part = []

        def backtrack(i):

            if i>= len(s):
                res.append(part.copy())
                return
            for j in range(i, len(s)):
                if self.isPali(s, i, j):
                    part.append(s[i:j+1])
                    backtrack(j+1)
                    part.pop()
        
        backtrack(0)
        return res

    def isPali(self, s, l, h):
        while ( l< h ):
            if s[l] != s[h]:
                return False
            l = l+1
            h = h-1
        return True

# Instantiate the Solution class
solution = Solution()

# Test Case 1
s1 = "aab"
print("Input:", s1)
print("Output:", solution.partition(s1))  # Expected: [["a", "a", "b"], ["aa", "b"]]

# Test Case 2
s2 = "a"
print("\nInput:", s2)
print("Output:", solution.partition(s2))  # Expected: [["a"]]

# Test Case 3
s3 = "aaa"
print("\nInput:", s3)
print("Output:", solution.partition(s3))  
# Expected: [["a", "a", "a"], ["a", "aa"], ["aa", "a"], ["aaa"]]

# Test Case 4
s4 = "racecar"
print("\nInput:", s4)
print("Output:", solution.partition(s4))  
# Expected: [["r", "a", "c", "e", "c", "a", "r"], ["r", "aceca", "r"], ["racecar"]]

# Test Case 5
s5 = "abcd"
print("\nInput:", s5)
print("Output:", solution.partition(s5))  
# Expected: [["a", "b", "c", "d"]] (No substrings are palindromes except individual characters)

# Test Case 6
s6 = "aba"
print("\nInput:", s6)
print("Output:", solution.partition(s6))  
# Expected: [["a", "b", "a"], ["aba"]]

# Test Case 7
s7 = "ababbb"
print("\nInput:", s7)
print("Output:", solution.partition(s7))  
# Expected: [["a", "b", "a", "b", "b", "b"], ["a", "b", "a", "bb", "b"], ["a", "bab", "b", "b"], ["a", "b", "abb", "b"]]
