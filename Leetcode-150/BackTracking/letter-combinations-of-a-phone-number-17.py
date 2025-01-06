"""
    Given a string containing digits from 2-9 inclusive, return all possible letter
    combinations that the number could represent. Return the answer in any order.
    A mapping of digits to letters (just like on the telephone buttons) is given below.
    Note that 1 does not map to any letters.
    Input: digits = "34"
    Output: ["dg","dh","di","eg","eh","ei","fg","fh","fi"]
"""
from typing import List
class Solution:
    """
        if we take "23" 23 would have three choices at each level look at the DT to understand it better.

                            "" (start)
                 ___________/ | \__________
                /            |             |
              "a"           "b"           "c"   \(Choose from "2")
            /  |  \       /  |  \       /  |       |
         "ad" "ae" "af" "bd" "be" "bf" "cd" "ce" "cf"   (Choose from "3")

    """
    def letterCombinations(self, digits: str) -> List[str]:
        phone_numbers = {
            "2" : "abc",
            "3" : "def",
            "4" : "ghi",
            "5" : "jkl",
            "6" : "mno",
            "7" : "pqrs",
            "8" : "tuv",
            "9" : "wxyz",
        }

        res = []
        def backTrack(i, currStr):
            if len(currStr) == len(digits):
                res.append(currStr)
                return
            
            for c in phone_numbers[digits[i]]:
                backTrack(i+1,currStr+c)
            
        if digits:
            backTrack(0,"")
        return res
    
def test_letter_combinations():
    solution = Solution()
    
    # Test Case 1: Single digit
    result = solution.letterCombinations("2")
    expected = ["a", "b", "c"]
    assert sorted(result) == sorted(expected), f"Failed Test Case 1: {result}"

    # Test Case 2: Two digits
    result = solution.letterCombinations("23")
    expected = ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
    assert sorted(result) == sorted(expected), f"Failed Test Case 2: {result}"

    # Test Case 3: Three digits
    result = solution.letterCombinations("456")
    expected = [
        "gjm", "gjn", "gjo", "gkm", "gkn", "gko", "glm", "gln", "glo",
        "hjm", "hjn", "hjo", "hkm", "hkn", "hko", "hlm", "hln", "hlo",
        "ijm", "ijn", "ijo", "ikm", "ikn", "iko", "ilm", "iln", "ilo",
    ]
    assert sorted(result) == sorted(expected), f"Failed Test Case 3: {result}"

    # Test Case 4: No digits (empty string)
    result = solution.letterCombinations("")
    expected = []
    assert result == expected, f"Failed Test Case 4: {result}"

    # Test Case 5: Edge case - input with a single repeated digit
    result = solution.letterCombinations("22")
    expected = ["aa", "ab", "ac", "ba", "bb", "bc", "ca", "cb", "cc"]
    assert sorted(result) == sorted(expected), f"Failed Test Case 5: {result}"

    # Test Case 6: Large input (all digits from 2 to 9)
    result = solution.letterCombinations("234")
    # Length of the result should be product of mappings: 3 * 3 * 3 = 27
    assert len(result) == 27, f"Failed Test Case 6: {result}"

    print("All test cases passed!")


test_letter_combinations()