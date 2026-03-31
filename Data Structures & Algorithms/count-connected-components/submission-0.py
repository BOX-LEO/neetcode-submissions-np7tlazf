class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        edges_map = defaultdict(list)
        for i,j in edges:
            edges_map[i].append(j)
            edges_map[j].append(i)

        visited = set()
        res = 0
        def dfs(node):
            visited.add(node)
            for n in edges_map[node]:
                if n not in visited:
                    dfs(n)
                    
        for i in range(n):
            if i not in visited:
                dfs(i)
                res+=1
        return res