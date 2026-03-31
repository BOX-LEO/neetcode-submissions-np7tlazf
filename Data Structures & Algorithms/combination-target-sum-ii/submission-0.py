class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []
        length = len(candidates)
        def dfs(ind,temp):
            # print(temp)
            if sum(temp)>target:
                return
            elif sum(temp)==target:
                print(temp)
                result.append(temp.copy())
            else:
                if ind==length:
                    return 
                temp.append(candidates[ind])
                dfs(ind+1,temp)
                temp.pop()
                while ind+1<length and candidates[ind+1]==candidates[ind]:
                    ind+=1
                dfs(ind+1,temp)
        dfs(0,[])
        return result