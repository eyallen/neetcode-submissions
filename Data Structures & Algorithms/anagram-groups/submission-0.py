from collections import defaultdict

class Solution:
    def stringToKey(self, string: str) -> tuple:
        key = [0] * 26

        for char in string:
            index = ord(char) - ord('a')
            key[index] += 1
        
        return tuple(key)


    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        str_map = defaultdict(list)

        for string in strs:
            key = self.stringToKey(string)

            str_map[key].append(string)
        
        output = []
        for key in str_map:
            output.append(str_map[key])

        return output

