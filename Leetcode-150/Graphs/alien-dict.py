from typing import List
class Solution:
    def findOrder(self, dict: List[str], k : int) -> str:

        n = len(dict)
        adj = [[] for _ in range(k)] # [[], [], [], ....k[]]
        for i in range(1, n):
            f = dict[i-1]
            s = dict[i]
            minLen = min(len(f), len(s))
            for i in range(minLen):
                if f[i] != s[i]:
                    n1 = ord(f[i]) - ord('a') 
                    n2 = ord(s[i]) - ord('a') 
                    adj[n1].append(n2)
                    break
        
        stack = []
        v = [0]*k

        def dfs(i):
            v [i] = 1
            for ne in adj[i]:
                if v[ne] != 1:
                    dfs(ne)
            stack.append(i)

        for i in range(k):
            if v[i] == 0:
                dfs(i)
        
        result = ""
        while stack:
            result += chr(stack.pop() + ord('a'))
        
        return result

def test():
    sol = Solution()
    dict = ["baa", "abcd", "abca", "cab", "cad"]
    res  = sol.findOrder(dict, 4)
    print(res)

if __name__ == "__main__":
    test()

        
        

            
