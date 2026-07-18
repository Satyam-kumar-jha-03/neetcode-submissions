from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        set = defaultdict(list)
        arr = []

        for i in strs:
            s = sorted(i)
            set[tuple(s)].append(i)

        for i in set.values():
            arr.append(i) 

        return arr
        