class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        graph = defaultdict(set)
        for i,j in edges:
            graph[i].add(j)
            graph[j].add(i)
        visited = set()
        self.res = n
        def dfs(node):
            visited.add(node)
            for i in graph[node]:
                if i not in visited:
                    dfs(i)
                    # graph[node].remove(i)
                    # if len(graph[node])==0:
                    #     del graph[node]
                    # graph[i].remove(node)
                    # if len(graph[i])==0:
                    #     del graph[i]
                    self.res-=1
        for i in range(n):
            if i in graph:
                dfs(i)
        return self.res