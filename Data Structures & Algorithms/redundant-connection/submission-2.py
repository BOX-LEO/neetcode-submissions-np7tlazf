class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parents = list(range(len(edges)))
        rank = [0]*len(edges)
        def find(n):
            if parents[n]!=n:
                # not root
                parents[n] = find(parents[n])
            return parents[n]
        def union(a,b):
            pa,pb = find(a),find(b)
            if pa==pb:
                return False
            if rank[pa]<rank[pb]:
                parents[pa]=pb
            elif rank[pa]>rank[pb]:
                parents[pb]=pa
            else:
                parents[pb]=pa
                rank[pa]+=1
            return True
        for n1,n2 in edges:
            if not union(n1-1,n2-1):
                return [n1,n2]
