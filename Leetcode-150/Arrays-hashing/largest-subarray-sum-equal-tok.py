class Solution:
    def longestSubarray(self, arr, k):
        # code here
        n = len(arr)
        max_len = 0
        seen = {}
        x = 0
        for i in range(n):
            x += arr[i]
            if x == k:
                max_len = i + 1

            else:
                rem = x - k
                if rem in seen:
                    max_len = max(i - seen[rem], max_len)

            if x not in seen:
                seen[x] = i
        return max_len
