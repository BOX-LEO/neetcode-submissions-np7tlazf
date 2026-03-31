class Solution:

    def encode(self, strs: List[str]) -> str:
        self.string=''
        for s in strs:
            self.string+= s+'/'
        return self.string

    def decode(self, s: str) -> List[str]:
        return s.split('/')[:-1]



