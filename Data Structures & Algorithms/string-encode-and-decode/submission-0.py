class Solution:

    def encode(self, strs: List[str]) -> str:
        pieces = []

        for s in strs:
            p = f"{len(s)}:{s}"
            pieces.append(p)
        
        return "".join(pieces)


    def decode(self, s: str) -> List[str]:
        out = []

        i = 0
        while i < len(s):
            j = s.find(":", i)
            length = int(s[i:j])
            word = s[j+1 : j+1+length]
            i = j + 1 + length

            out.append(word)
        
        return out
