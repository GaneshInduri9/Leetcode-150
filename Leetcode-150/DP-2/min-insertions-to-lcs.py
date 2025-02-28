def lcs(s1, s2):
    n = len(s1)
    m = len(s2)

    # Initialize a 2D array to store the length of the Longest Common Subsequence (LCS)
    dp = [[-1 for i in range(m + 1)] for j in range(n + 1)]

    # Base cases: When one of the strings is empty, LCS length is 0.
    for i in range(n + 1):
        dp[i][0] = 0
    for i in range(m + 1):
        dp[0][i] = 0

    # Fill in the dp array using dynamic programming
    for ind1 in range(1, n + 1):
        for ind2 in range(1, m + 1):
            if s1[ind1 - 1] == s2[ind2 - 1]:
                dp[ind1][ind2] = 1 + dp[ind1 - 1][ind2 - 1]
            else:
                dp[ind1][ind2] = max(dp[ind1 - 1][ind2], dp[ind1][ind2 - 1])

    # The final value in dp will be the length of the LCS
    return dp[n][m]


def longestPalindromeSubsequence(s):
    # Reverse the input string
    t = s
    s = s[::-1]

    # Find the length of the longest common subsequence between s and its reverse
    return lcs(s, t)


def minInsertion(s):
    n = len(s)

    # Calculate the length of the longest palindromic subsequence
    k = longestPalindromeSubsequence(s)

    # The minimum insertions required to make the string palindrome is the difference between its length and the length of its longest palindromic subsequence
    return n - k


def main():
    s = "abcaa"
    print(
        "The Minimum insertions required to make the string palindrome:",
        minInsertion(s),
    )


if __name__ == "__main__":
    main()
