class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def string2label(string):
            l = [0]*26
            for c in string:
                l[ord(c)-ord('a')]+=1
            return l

        output = {}
        for s in strs:
            try:
                output[tuple(string2label(s))].append(s)
            except:
                output[tuple(string2label(s))] = [s]
        
        return [i for i in output.values()]
            
        
       