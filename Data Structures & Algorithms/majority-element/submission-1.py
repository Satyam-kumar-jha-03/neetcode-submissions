import statistics as stats
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        return(stats.mode(nums))
        
        