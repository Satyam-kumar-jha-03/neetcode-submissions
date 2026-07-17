from collections import defaultdict
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        set = defaultdict(list)

        for num in nums:
            s = num
            set[s].append(num)

        if len(set) == len(nums):
            return False
        else:
            return True