class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        r = 0
        s1_len = len(s1)
        s2_len = len(s2)
        s2_map = [0]*26
        s1_map = [0]*26
        for i in range(s1_len):
            s1_map[ord(s1[i]) -ord('a')] += 1
        
        while r < s2_len:
            s2_map[ord(s2[r])- ord('a')] += 1
            if (r-l)+1 == s1_len:
                if self.checkAnangarms(s1_map, s2_map):
                    return True
                s2_map[ord(s2[l])- ord('a')] -= 1
                l = l+ 1
            
            r += 1
        return False
    def checkAnangarms(self, s1_map, s2_map):
        for i in range(26):
            if s1_map[i] != s2_map[i]:
                return False
        return True
            