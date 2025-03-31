class Solution:
    def findTheCity(
        self, n: int, edges: List[List[int]], distanceThreshold: int
    ) -> int:
        dist = [[float("inf") for _ in range(n)] for _ in range(n)]

        for i in range(n):
            dist[i][i] = 0
        for u, v, w in edges:
            dist[u][v] = w
            dist[v][u] = w

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    d = min(dist[i][j], dist[i][k] + dist[k][j])
                    dist[i][j] = d

        max_count = float("inf")
        city_ = -1
        for city in range(n):
            count = 0
            for adjcity in range(n):
                if city != adjcity and dist[city][adjcity] <= distanceThreshold:
                    count += 1

            if count <= max_count:
                max_count = count
                city_ = city
        return city_
