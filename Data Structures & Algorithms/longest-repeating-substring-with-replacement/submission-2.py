class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0,0
        table = defaultdict(int)
        result = 0
        while r<=len(s)-1:
            print(r)
            table[s[r]]+=1
            maxf = max(table.values())
            if r-l+1-maxf<=k:
                print('v')
                result=max(result,r-l+1)
                r+=1
            else:
                print('n')
                table[s[l]]-=1
                l+=1
                r+=1
        return result
        
        


        