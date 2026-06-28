class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        def backtrack(cur = [],index = 0,total = 0):
            if total == target:
                res.append(cur.copy())
                return
            elif total>target or index>=len(candidates):
                return
            temp = candidates[index]
            cur.append(temp)
            total+=temp
            backtrack(cur,index+1,total)
            cur.pop()
            total-=temp
            while index+1<len(candidates) and candidates[index+1]==candidates[index]:
                index+=1
            backtrack(cur,index+1,total)
        backtrack()
        return res