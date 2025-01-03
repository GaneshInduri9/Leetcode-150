"""
    Given two strings s and t of lengths m and n respectively, return the minimum window 
    substring of s such that every character in t (including duplicates) is included in 
    the window. If there is no such substring, return the empty string "".
    The testcases will be generated such that the answer is unique.
"""

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        minLen = float('inf')  # Track the minimum length of the window
        start = -1  # Track the starting index of the minimum window
        n = len(s)
        m = len(t)

        # Outer loop to define the starting index
        for i in range(n):
            hashMap = [0] * 256
            for char in t:
                hashMap[ord(char)] += 1
            
            count = 0

            # Inner loop to find the end of the window
            for j in range(i, n):
                if hashMap[ord(s[j])] > 0:
                    count += 1
                hashMap[ord(s[j])] -= 1

                # Check if we have a valid window
                if count == m:
                    if (j - i + 1) < minLen:
                        minLen = j - i + 1
                        start = i
                    break  # Stop expanding this window once a valid substring is found

        # If no valid window was found, return ""
        return "" if start == -1 else s[start:start + minLen]
    
    def minWindowOptimal(self, s: str, t: str)-> str:
        hash_map=[0] * 256
        minLen = float('inf')
        start = -1
        n = len(s)
        m = len(t)
        l = 0 
        r = 0
        count = 0
        for i in range(m):
            hash_map[ord(t[i])] += 1
        while r < n:
            if hash_map[ord(s[r])] > 0:
                count += 1
            hash_map[ord(s[r])] -= 1
            while count == m:
                if (r-l) + 1 < minLen:
                    minLen = (r-l) + 1
                    start = l
                hash_map[ord(s[l])] += 1

                if(hash_map[ord(s[l])]> 0):
                    count -= 1
                
                l += 1
            r += 1
        return "" if start == -1 else s[start:start + minLen]



            

