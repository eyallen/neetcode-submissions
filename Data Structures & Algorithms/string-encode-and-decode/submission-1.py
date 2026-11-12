class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""

        for s in strs:
            encoded += f"{len(s)}#{s}"
        
        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = []

        i = 0
        while i < len(s):
            hash_index = s.find("#", i)
            length = int(s[i:hash_index])
            start = hash_index + 1
            end = start + length
            decoded.append(s[start:end])
            i = end

        return decoded
