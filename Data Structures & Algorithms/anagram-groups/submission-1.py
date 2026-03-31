class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def get_count_key(word:str):
            key = [0]*26
            for c in word:
                ind = ord(c)-ord('a')
                key[ind]+=1
            return tuple(key)
        res = defaultdict(list)
        for s in strs:
            res[get_count_key(s)].append(s)

        return list(res.values())