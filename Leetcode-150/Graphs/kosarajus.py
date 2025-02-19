class Solution:

    def kosaraju(self, adj):

        V = len(adj)
        stack = []
        vis = [0] * V

        def dfs(i):
            vis[i] = 1
            for n in adj[i]:
                if vis[n] == 0:
                    dfs(n)

            stack.append(i)

        for i in range(V):
            if vis[i] == 0:
                dfs(i)

        adj_copy = [[] for _ in adj]

        for i in range(V):
            vis[i] = 0
            for nb in adj[i]:
                adj_copy[nb].append(i)

        def dfs1(i):
            vis[i] = 1

            for nb in adj_copy[i]:
                if vis[nb] == 0:
                    dfs1(nb)

        ans = 0
        print(stack)
        while stack:
            node = stack.pop()
            if vis[node] == 0:
                ans += 1
                dfs1(node)

        return ans


def test():
    adj = [[2, 3], [0], [1], [4], []]
    sol = Solution()
    res = sol.kosaraju(adj)
    print(res)


if __name__ == "__main__":
    test()
