class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        parent = list(range(n))
        rank = [1]*n

        def find(node):
            if parent[node]!=node:
                parent[node] = find(parent[node])
            return parent[node]
        def union(a,b):
            pa,pb = find(a),find(b)
            if pa==pb:
                return False
            if rank[pa]<rank[pb]:
                parent[pa] = pb
            elif rank[pa]>rank[pb]:
                parent[pb]=pa
            else:
                parent[pb]=pa
                rank[pa]+=1
            return True
        for i,j in edges:
            if union(i,j):
                continue
            else:
                return False
        return True

            