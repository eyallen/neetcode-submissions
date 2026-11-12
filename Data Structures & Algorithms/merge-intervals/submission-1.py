from itertools import pairwise

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        result: list[list[int]] = []
        intervals.sort(key= lambda iv: iv[0])

        for interval in intervals:
            if len(result) == 0:
                result.append(interval)
                continue
            
            last = result[-1]
            # check for overlap
            if last[1] >= interval[0]:
                last[1] = max(last[1], interval[1])
            else:
                result.append(interval)

        return result
