from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        set = defaultdict(int)
        for num in nums:
            set[num] += 1
        
        b = sorted(set, key  =  set.get,reverse = True)[:k]
        b.sort()

        return b

        